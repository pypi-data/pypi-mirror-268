use std::collections::HashMap;

use numpy::{PyArray1, PyArrayMethods};
use pyo3::{exceptions::PyValueError, prelude::*, types::PyDict};

use crate::{AgentId, Position, Renderer, Tile, World, WorldState};

use super::{
    pyaction::PyAction,
    pyagent::PyAgent,
    pyevent::PyWorldEvent,
    pyexceptions::{parse_error_to_exception, runtime_error_to_pyexception},
    pytile::{PyGem, PyLaser, PyLaserSource},
    pyworld_state::PyWorldState,
};

#[pyclass(name = "World", module = "lle")]
pub struct PyWorld {
    world: World,
    renderer: Renderer,
}

unsafe impl Send for PyWorld {}

impl PyWorld {
    pub fn from_world(world: World) -> Self {
        let renderer = Renderer::new(&world);
        PyWorld { world, renderer }
    }
}

#[pymethods]
impl PyWorld {
    #[new]
    pub fn new(map_str: String) -> PyResult<Self> {
        let world = match World::try_from(map_str) {
            Ok(world) => world,
            Err(e) => return Err(parse_error_to_exception(e)),
        };
        let renderer = Renderer::new(&world);
        Ok(PyWorld { world, renderer })
    }

    #[staticmethod]
    fn from_file(filename: String) -> PyResult<Self> {
        let world = match World::from_file(&filename) {
            Ok(world) => world,
            Err(e) => return Err(parse_error_to_exception(e)),
        };
        let renderer = Renderer::new(&world);
        Ok(PyWorld { world, renderer })
    }

    #[staticmethod]
    fn level(level: usize) -> PyResult<Self> {
        match World::get_level(level) {
            Ok(world) => {
                let renderer = Renderer::new(&world);
                Ok(PyWorld { world, renderer })
            }
            Err(err) => Err(parse_error_to_exception(err)),
        }
    }

    #[getter]
    fn world_string(&self) -> String {
        self.world.world_string().into()
    }

    #[getter]
    pub fn n_agents(&self) -> usize {
        self.world.n_agents()
    }

    #[getter]
    /// Return the rendering dimensions (width, height)
    pub fn image_dimensions(&self) -> (u32, u32) {
        (self.renderer.pixel_width(), self.renderer.pixel_height())
    }

    #[getter]
    pub fn width(&self) -> usize {
        self.world.width()
    }

    #[getter]
    pub fn height(&self) -> usize {
        self.world.height()
    }

    #[getter]
    pub fn n_gems(&self) -> usize {
        self.world.n_gems()
    }

    #[getter]
    /// The list of the positions of the void tiles
    pub fn void_pos(&self) -> Vec<Position> {
        self.world.void_positions().copied().collect()
    }

    #[getter]
    /// The number of gems collected so far (since the last reset).
    fn gems_collected(&self) -> usize {
        self.world.n_gems_collected()
    }

    #[getter]
    /// The positions of the agents.
    fn agents_positions(&self) -> Vec<Position> {
        self.world.agents_positions().clone()
    }

    #[getter]
    /// The positions of the wall tiles.
    fn wall_pos(&self) -> Vec<Position> {
        self.world.walls().copied().collect()
    }

    #[getter]
    /// The gems with their respective position.
    fn gems(&self) -> HashMap<Position, PyGem> {
        self.world
            .gems()
            .map(|(pos, gem)| (*pos, PyGem::new(gem.agent(), gem.is_collected())))
            .collect()
    }

    #[getter]
    /// The lasers with their respective position.
    fn lasers(&self) -> Vec<(Position, PyLaser)> {
        self.world
            .lasers()
            .map(|(pos, laser)| (*pos, PyLaser::from(laser)))
            .collect()
    }

    #[getter]
    /// The laser sources with their respective position.
    fn laser_sources(&self) -> HashMap<Position, PyLaserSource> {
        self.world
            .laser_sources()
            .map(|(pos, laser_source)| (*pos, PyLaserSource::from(laser_source)))
            .collect()
    }

    fn disable_laser_source(&self, laser_source: &PyLaserSource) -> PyResult<()> {
        let id = laser_source.laser_id();
        if let Some((_, source)) = self.world.laser_sources().find(|(_, l)| l.laser_id() == id) {
            source.disable();
            return Ok(());
        }
        return Err(PyValueError::new_err(format!(
            "Laser source with laser_id {id} not found"
        )));
    }

    fn enable_laser_source(&self, laser_source: &PyLaserSource) -> PyResult<()> {
        let id = laser_source.laser_id();
        if let Some((_, source)) = self.world.laser_sources().find(|(_, l)| l.laser_id() == id) {
            source.enable();
            return Ok(());
        }
        Err(PyValueError::new_err(format!(
            "Laser source with laser_id {id} not found"
        )))
    }

    fn set_laser_colour(&self, laser_source: &PyLaserSource, new_colour: i32) -> PyResult<()> {
        let new_colour = match AgentId::try_from(new_colour) {
            Ok(r) => r,
            Err(_) => {
                return Err(PyValueError::new_err(format!(
                    "New colour {new_colour} must be >= 0"
                )))
            }
        };
        if new_colour >= self.world.n_agents() {
            let n_agents = self.world.n_agents();
            return Err(PyValueError::new_err(format!(
                "New colour {new_colour} does not belong to an existing agent !\nThere are {n_agents} agents in the world, provide a value bewteen 0 and {} included.",
                n_agents -1
            )));
        }
        let id = laser_source.laser_id();
        if let Some((_, source)) = self.world.laser_sources().find(|(_, l)| l.laser_id() == id) {
            source.set_agent_id(new_colour);
            return Ok(());
        }
        Err(PyValueError::new_err(format!(
            "Laser source with laser_id {id} not found"
        )))
    }

    #[getter]
    /// The positions of the exit tiles.
    fn exit_pos(&self) -> Vec<Position> {
        self.world.exits().map(|(pos, _)| pos).copied().collect()
    }

    #[getter]
    fn start_pos(&self) -> Vec<Position> {
        self.world.starts().collect()
    }

    /// Perform a step in the world and returns the events that happened during that transition.
    pub fn step(&mut self, actions: Vec<PyAction>) -> PyResult<Vec<PyWorldEvent>> {
        let actions: Vec<_> = actions.into_iter().map(|a| a.action).collect();
        match self.world.step(&actions) {
            Ok(events) => {
                let events: Vec<PyWorldEvent> =
                    events.iter().map(|e| PyWorldEvent::from(e)).collect();
                Ok(events)
            }
            Err(e) => Err(runtime_error_to_pyexception(e)),
        }
    }

    /// Reset the world to its original state.
    pub fn reset(&mut self) {
        self.world.reset();
    }

    /// Return the available actions for each agent.
    /// `world.available_actions()[i]` is the list of available actions for agent i.
    pub fn available_actions(&self) -> Vec<Vec<PyAction>> {
        self.world
            .available_actions()
            .iter()
            .map(|a| a.iter().map(|a| PyAction { action: a.clone() }).collect())
            .collect()
    }

    #[getter]
    /// Return the list of agents.
    pub fn agents(&self) -> Vec<PyAgent> {
        self.world
            .agents()
            .iter()
            .map(|a| PyAgent { agent: a.clone() })
            .collect()
    }

    /// Renders the world as an image and returns it in a numpy array.
    fn get_image(&self, py: Python) -> PyResult<PyObject> {
        let dims = self.image_dimensions();
        let dims = (dims.1 as usize, dims.0 as usize, 3);
        let img = self.renderer.update(&self.world);
        let buffer = img.into_raw();
        let res = PyArray1::from_vec_bound(py, buffer)
            .reshape(dims)
            .unwrap_or_else(|_| panic!("Could not reshape the image to {dims:?}"));
        Ok(res.into_py(py))
    }

    /// Force the world to a specific state
    fn set_state(&mut self, state: PyWorldState) -> PyResult<Vec<PyWorldEvent>> {
        match self.world.set_state(&state.into()) {
            Ok(events) => Ok(events.iter().map(|e| PyWorldEvent::from(e)).collect()),
            Err(e) => Err(runtime_error_to_pyexception(e)),
        }
    }

    /// Return the current state of the world (that can be set with `world.set_state`)
    fn get_state(&self) -> PyWorldState {
        let state = self.world.get_state();
        PyWorldState::new(state.agents_positions, state.gems_collected)
    }

    pub fn __deepcopy__(&self, _memo: &Bound<PyDict>) -> Self {
        self.clone()
    }

    /// This method is called to instantiate the object before deserialisation.
    /// It required "default arguments" to be provided to the __new__ method
    /// before replacing them by the actual values in __setstate__.
    pub fn __getnewargs__(&self) -> PyResult<(String,)> {
        Ok((String::from("S0 X"),))
    }

    /// Enable serialisation with pickle
    pub fn __getstate__(&self) -> PyResult<(String, Vec<bool>, Vec<Position>)> {
        let state = self.world.get_state();
        let data = (
            self.world.world_string().to_owned(),
            state.gems_collected.clone(),
            state.agents_positions.clone(),
        );
        Ok(data)
    }

    pub fn __setstate__(&mut self, state: (String, Vec<bool>, Vec<Position>)) -> PyResult<()> {
        self.world = match World::try_from(state.0) {
            Ok(core) => core,
            Err(e) => panic!("Could not parse the world: {:?}", e),
        };
        self.renderer = Renderer::new(&self.world);
        self.world
            .set_state(&WorldState {
                gems_collected: state.1,
                agents_positions: state.2,
            })
            .unwrap();
        Ok(())
    }
}

impl Clone for PyWorld {
    fn clone(&self) -> Self {
        let core = self.world.clone();
        let renderer = Renderer::new(&core);
        PyWorld {
            world: core,
            renderer,
        }
    }
}
