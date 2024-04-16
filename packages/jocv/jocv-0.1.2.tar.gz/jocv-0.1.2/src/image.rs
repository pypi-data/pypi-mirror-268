use glam::{DVec2, DVec3, DQuat};
use pyo3::pyclass;
use crate::types::{image_t, camera_t, point3D_t};

#[pyclass]
pub struct Image {
    #[pyo3(get)]
    pub image_id: image_t,
    #[pyo3(get)]
    pub camera_id: camera_t,
    #[pyo3(get)]
    pub name: String,
    pub rot: DQuat,
    pub trans: DVec3,
    #[allow(non_snake_case)]
    pub points2D: Vec<DVec2>,
    #[pyo3(get)]
    pub point3D_ids: Vec<point3D_t>,
}