cmake_minimum_required(VERSION 3.15.0)

project(pcd_reader)

find_package(PCL 1.9 REQUIRED)

include_directories(${PCL_INCLUDE_DIRS})
link_directories(${PCL_LIBRARY_DIRS})
add_definitions(${PCL_DEFINITIONS})

add_executable(pcd_reader pcd_reader.cpp)
target_link_libraries(pcd_reader ${PCL_LIBRARIES})
