
//use ahash::AHashMap;
use std::collections::HashMap;
use crate::types::image_t;
use crate::point3d::Point3D;

pub fn compute_overlaps(points3D: Vec<Point3D>, num_images: usize) -> Vec<HashMap<image_t, image_t>>{
    println!("Making sets...");
    let mut shared_points: Vec<HashMap<image_t, image_t>> = Vec::with_capacity(num_images);
    for _ in 0..num_images{shared_points.push(HashMap::new())};
    
    for point in points3D{
        for i in 0..point.track.len(){
            for j in 0..i {
                let im_i = point.track[i].0;
                let im_j = point.track[j].0;
                *shared_points[im_i as usize].entry(im_j).or_insert(0) += 1;
                *shared_points[im_j as usize].entry(im_i).or_insert(0) += 1;
            } 
        }
    }
    println!("Done!");
    return shared_points
}
