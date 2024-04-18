
use ahash::RandomState;
use std::collections::HashMap;
use crate::types::{image_t,point3D_t};
use crate::point3d::Point3D;

pub fn compute_overlaps(points3D: HashMap<point3D_t, Point3D, RandomState>) -> HashMap<image_t, HashMap<image_t, image_t, RandomState>, RandomState>{
    println!("Making sets...");
    let mut shared_points: HashMap<image_t, HashMap<image_t, image_t, RandomState>, RandomState> = HashMap::default();
    
    for (_, point) in points3D{
        for i in 0..point.track.len(){
            for j in 0..i+1 {
                let im_i = point.track[i].0;
                let im_j = point.track[j].0;
                *shared_points.entry(im_i).or_insert(HashMap::default()).entry(im_j).or_insert(0) += 1;
                *shared_points.entry(im_j).or_insert(HashMap::default()).entry(im_i).or_insert(0) += 1;
            } 
        }
    }
    println!("Done!");
    return shared_points
}
