#include <iostream>
#include <pcl/io/pcd_io.h>
#include <pcl/point_types.h>
#include <pcl/visualization/pcl_visualizer.h>
#include <thread>
#include <chrono>

using Visualizer = pcl::visualization::PCLVisualizer;
using namespace std::literals::chrono_literals;

void iterate_over_cloud(pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_ptr) {
	for (int i=0; i<10; i++) {
		const auto& point = cloud_ptr->points[i];
		std::cout << " " << point.x
				  << " " << point.y 
				  << " " << point.z << std::endl;
	}
	
}

pcl::visualization::PCLVisualizer::Ptr simpleVis(
pcl::PointCloud<pcl::PointXYZRGB>::ConstPtr cloud, std::string cloud_name) {
	pcl::visualization::PCLVisualizer::Ptr p_visualizer 
	(new pcl::visualization::PCLVisualizer("KAI - Point Cloud Viewer"));
	p_visualizer->setBackgroundColor(0, 0, 0);
	p_visualizer->addPointCloud<pcl::PointXYZRGB> (cloud, cloud_name);
	p_visualizer->setPointCloudRenderingProperties (pcl::visualization::PCL_VISUALIZER_POINT_SIZE, 1, cloud_name);
	p_visualizer->addCoordinateSystem(1.0);
	p_visualizer->initCameraParameters();
	return p_visualizer;

}

int main (int argc, char ** argv) {
	pcl::PointCloud<pcl::PointXYZRGB>::Ptr cloud_ptr
	(new pcl::PointCloud<pcl::PointXYZRGB>);

	int success = pcl::io::loadPCDFile<pcl::PointXYZRGB>("../GP_trolley.pcd", *cloud_ptr);
	if (success != 0) {
		std::cout << "could not load GP_trolley.pcd file" << std::endl;
		return -1;
	}

	std::cout << "loaded " << cloud_ptr->width * cloud_ptr->height <<
				" data points from GP_trolley.pcd" << std::endl;
	iterate_over_cloud(cloud_ptr);

	Visualizer::Ptr p_viewer;
	p_viewer = simpleVis(cloud_ptr, "trolley_cloud");

	// main loop
	while (!p_viewer->wasStopped ()) {
		p_viewer->spinOnce (100);
		std::this_thread::sleep_for(100ms);
	}

}
