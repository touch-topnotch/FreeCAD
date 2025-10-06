cmake_minimum_required(VERSION 3.20)
project(archi-launcher LANGUAGES CXX)

set(CMAKE_OSX_DEPLOYMENT_TARGET "10.13" CACHE STRING "Minimum OS X deployment version" FORCE)
set(CMAKE_CXX_STANDARD 17)

add_executable(ARCHI FreeCAD.cpp)
target_link_libraries(ARCHI)
