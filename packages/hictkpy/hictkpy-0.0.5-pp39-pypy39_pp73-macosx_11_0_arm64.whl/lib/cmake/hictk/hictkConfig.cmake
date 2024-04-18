# Copyright (C) 2023 Roberto Rossini <roberros@uio.no>
#
# SPDX-License-Identifier: MIT


####### Expanded from @PACKAGE_INIT@ by configure_package_config_file() #######
####### Any changes to this file will be overwritten by the next CMake run ####
####### The input file was hictkConfig.cmake.in                            ########

get_filename_component(PACKAGE_PREFIX_DIR "${CMAKE_CURRENT_LIST_DIR}/../../../" ABSOLUTE)

macro(set_and_check _var _file)
  set(${_var} "${_file}")
  if(NOT EXISTS "${_file}")
    message(FATAL_ERROR "File or directory ${_file} referenced by variable ${_var} does not exist !")
  endif()
endmacro()

macro(check_required_components _NAME)
  foreach(comp ${${_NAME}_FIND_COMPONENTS})
    if(NOT ${_NAME}_${comp}_FOUND)
      if(${_NAME}_FIND_REQUIRED_${comp})
        set(${_NAME}_FOUND FALSE)
      endif()
    endif()
  endforeach()
endmacro()

####################################################################################

set(HICTK_WITH_EIGEN OFF)

include(CMakeFindDependencyMacro)

find_dependency(
  bshoshany-thread-pool
  CONFIG
  QUIET
  REQUIRED)
find_dependency(
  concurrentqueue
  CONFIG
  QUIET
  REQUIRED)

if(HICTK_WITH_EIGEN)
  find_dependency(
    Eigen3
    CONFIG
    QUIET
    REQUIRED)
endif()

find_dependency(
  FastFloat
  CONFIG
  QUIET
  REQUIRED)
find_dependency(
  FMT
  CONFIG
  QUIET
  REQUIRED)
find_dependency(
  HDF5
  CONFIG
  QUIET
  REQUIRED
  COMPONENTS
  C)
find_dependency(
  HighFive
  CONFIG
  QUIET
  REQUIRED)
find_dependency(
  libdeflate
  CONFIG
  QUIET
  REQUIRED)
find_dependency(
  phmap
  CONFIG
  QUIET
  REQUIRED)
find_dependency(
  readerwriterqueue
  CONFIG
  QUIET
  REQUIRED)
find_dependency(
  span-lite
  CONFIG
  QUIET
  REQUIRED)
find_dependency(
  spdlog
  CONFIG
  QUIET
  REQUIRED)
find_dependency(
  zstd
  CONFIG
  QUIET
  REQUIRED)

include("${CMAKE_CURRENT_LIST_DIR}/hictkTargets.cmake")

check_required_components(hictk)
