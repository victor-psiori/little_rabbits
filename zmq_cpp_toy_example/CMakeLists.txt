cmake_minimum_required(VERSION 3.15)
project(zmq_cpp_toy LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_FLAGS "-Wall -Wextra -Wshadow -Wnon-virtual-dtor")
find_package(cppzmq REQUIRED)
find_package(nlohmann_json 3.2.0 REQUIRED)

add_executable(zmq_cpp_toy so_test_client.cpp)

target_include_directories(zmq_cpp_toy SYSTEM PUBLIC ${CPPZMQ_INCLUDE_DIR})
target_link_libraries(zmq_cpp_toy cppzmq nlohmann_json::nlohmann_json)