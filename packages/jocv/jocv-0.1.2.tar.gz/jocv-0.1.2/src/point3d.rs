use glam::DVec3;
use pyo3::prelude::*;
use crate::{track::TrackElement, types::{Color, point3D_t}};


#[pyclass]
#[derive(Clone)]
pub struct Point3D {
    pub point3D_id: point3D_t, 
    pub xyz: DVec3,
    pub color: Color,
    pub error: f64,
    pub track: Vec<TrackElement>,
}


#[pymethods]
impl Point3D {
    #[getter]
    fn get_id(&self) -> PyResult<point3D_t> {
        Ok(self.point3D_id)
    }
    #[getter]
    fn get_xyz(&self) -> PyResult<Vec<f64>> {
        Ok(self.xyz.as_ref().to_vec())
    }
    #[getter]
    fn get_color(&self) -> PyResult<Color> {
        Ok(self.color.clone())
    }
    #[getter]
    fn get_error(&self) -> PyResult<f64> {
        Ok(self.error)
    }
    #[getter]
    fn get_track(&self) -> PyResult<Vec<TrackElement>> {
        Ok(self.track.clone())
    }
    fn __str__(&self) -> PyResult<String>   {
        Ok(format!("Point3D with ID: {}, XYZ: {:.3}, and track length {}", self.point3D_id, self.xyz, self.track.len()))
    }
    fn __repr__(&self) -> PyResult<String> {
        Ok(format!("Point3D with ID: {}, XYZ: {:.3}, and track length {}", self.point3D_id, self.xyz, self.track.len()))
    }
}
