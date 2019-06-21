# MyApsIsticLuaLib
# Copyright © 2016 François Bodin
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library. If not, see <http://www.gnu.org/licenses/>.
#
# Modules can use a different licence.

## CMake Settings ##
cmake_minimum_required(VERSION 2.8)

project(MYAPSISTIC C CXX)

set(MYAPSISTIC_VERSION_MAJOR 0)
set(MYAPSISTIC_VERSION_MINOR 2)
set(MYAPSISTIC_VERSION_PATCH 0)
set(MYAPSISTIC_VERSION_STRING ${MYAPSISTIC_VERSION_MAJOR}.${MYAPSISTIC_VERSION_MINOR}.${MYAPSISTIC_VERSION_PATCH})

set(CMAKE_MODULE_PATH ${CMAKE_MODULE_PATH} "${MYAPSISTIC_SOURCE_DIR}/cmake/Modules/")


## User definitions ##
option(USE_DOXYGEN "Generate code documentation" OFF)
option(USE_CLANG "Use clang compiler instead of gcc" OFF)

## Packages ##
find_package(Threads REQUIRED)
#find_package(Lua)
set(LUA "/usr/include/lua5.2")
set(LUA_INCLUDE_DIR "/usr/include/lua5.2")
set(LUALIB "/usr/lib/lua/5.2")
set(LUABIN "/usr/bin")
set(LUA_VERSION_MAJOR 5)
set(LUA_VERSION_MINOR 2)
set(LUA_FOUND TRUE)

find_package(CURL 7.0.0)
find_package(Doxygen)

# Import the default install directories
find_file(GNU_INSTALL_DIRS_FROM_CMAKE NAMES GNUInstallDirs.cmake PATHS ${CMAKE_ROOT}/Modules)
mark_as_advanced(GNU_INSTALL_DIRS_FROM_CMAKE)
if(GNU_INSTALL_DIRS_FROM_CMAKE)
  include(${CMAKE_ROOT}/Modules/GNUInstallDirs.cmake)
else()
  include(${CMAKE_MODULE_PATH}/GNUInstallDirs.cmake)
endif()

## Debug: print all declared variables
# get_cmake_property(_variableNames VARIABLES)
# foreach (_variableName ${_variableNames})
# 	message(STATUS "${_variableName}=${${_variableName}}")
# endforeach()


## Compiler Infos ##

if(USE_CLANG)
	set(CMAKE_C_COMPILER "/usr/bin/clang")
	set(CMAKE_CXX_COMPILER "/usr/bin/clang++")
endif()

add_definitions("-Wall") # Not compatible with MSVC

set(CMAKE_C_FLAGS "${CMAKE_C_FLAGS} -std=gnu99")
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -ftest-coverage -fprofile-arcs")

### C++11 ###
include(CheckCXXCompilerFlag)
check_cxx_compiler_flag("-std=c++11" COMPILER_SUPPORTS_CXX11)
check_cxx_compiler_flag("-std=c++0x" COMPILER_SUPPORTS_CXX0X)
if(COMPILER_SUPPORTS_CXX11)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")
elseif(COMPILER_SUPPORTS_CXX0X)
	set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++0x")
else()
	message(STATUS "The compiler ${CMAKE_CXX_COMPILER} has no C++11 support. Please use a different C++ compiler.")
endif()

# Use rpath on Mac OS X
if(APPLE)
	cmake_policy(SET CMP0042 NEW)
endif()

## CMake input-output ##

set(CMAKE_BUILD_TYPE alpha)

set(CMAKE_LIBRARY_OUTPUT_DIRECTORY "build/${CMAKE_BUILD_TYPE}")
set(CMAKE_RUNTIME_OUTPUT_DIRECTORY "build/${CMAKE_BUILD_TYPE}")

include_directories("include/")

### Install paths ###

option(CMAKE_INSTALL_PREFIX "Prefix where MyApsIstic is installed" ${MYAPSISTIC_SOURCE_DIR})
set(LIBRARY_OUTPUT_PATH ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_LIBDIR})
set(BINARY_OUTPUT_PATH ${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_BINDIR})
set(INCLUDE_OUTPUT_PATH "${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_INCLUDEDIR}/MyApsIstic")
set(MYAPSISTIC_DOC_DIR "${CMAKE_INSTALL_PREFIX}/${CMAKE_INSTALL_DOCDIR}/MyApsIstic")

## Core Source files ##

set(
	CORE_SRC_FILES
	src/services.c
	src/jsmn.c
)

set(
	NETWORK_SRC_FILES
	src/network.c
)

set(
	LUA_SRC_FILES
	src/lua_bindings.c
)

set(
	SRC_FILES
	${CORE_SRC_FILES}
)

## Include Packages header and source files ##


if(CURL_FOUND)
	message(STATUS "Compiling with network interface")
	include_directories(${CURL_INCLUDE_DIRS})
	set(
		SRC_FILES
		${SRC_FILES}
		${NETWORK_SRC_FILES}
	)

	set(WITH_NETWORK ON)
else()
	message(STATUS "WITHOUT: curl network interface")
	set(WITH_NETWORK OFF)
endif()

if(LUA_FOUND AND LUA_VERSION_MAJOR EQUAL 5 AND
	(LUA_VERSION_MINOR EQUAL 1 OR LUA_VERSION_MINOR EQUAL 2 OR LUA_VERSION_MINOR EQUAL 3))
	message(STATUS "Compiling with Lua")
	include_directories(${LUA_INCLUDE_DIR})
	set(
		SRC_FILES
		${SRC_FILES}
		${LUA_SRC_FILES}
	)
else()
	message(WARNING "WITHOUT: Lua")
endif()

configure_file(${MYAPSISTIC_SOURCE_DIR}/include/common.h.in ${MYAPSISTIC_SOURCE_DIR}/include/common.h)

## Executables ##

add_library(
	myapsistic SHARED
	${SRC_FILES}
)

set_target_properties(myapsistic PROPERTIES C_VISIBILITY_PRESET hidden)
set_target_properties(myapsistic PROPERTIES CXX_VISIBILITY_PRESET hidden)
set_target_properties(myapsistic PROPERTIES VERSION ${MYAPSISTIC_VERSION_STRING} SOVERSION ${MYAPSISTIC_VERSION_MAJOR})


## Linking libraries ##

target_link_libraries(myapsistic ${CMAKE_THREAD_LIBS_INIT})

if(LUA_FOUND)
	target_link_libraries(myapsistic ${LUA_LIBRARIES})
endif()

if(WITH_NETWORK AND CURL_FOUND)
	target_link_libraries(myapsistic ${CURL_LIBRARIES})
endif()


if(USE_DOXYGEN AND DOXYGEN_FOUND)
	message(STATUS "Configure doc for Doxygen (run then 'doxygen doc/config-doxygen')")
	configure_file("${CMAKE_SOURCE_DIR}/doc/config-doxygen.in"
		"${CMAKE_SOURCE_DIR}/doc/config-doxygen"
		@ONLY)
	configure_file("${CMAKE_SOURCE_DIR}/doc/mainpage.doc.in"
		"${CMAKE_SOURCE_DIR}/doc/mainpage.doc"
		@ONLY)
else()
	message(WARNING "Doc NOT configured")
endif()


## Install ##

install(TARGETS myapsistic DESTINATION ${LIBRARY_OUTPUT_PATH})
if(LUA_FOUND)
	install(TARGETS myapsistic DESTINATION ${LIBRARY_OUTPUT_PATH}/lua/${LUA_VERSION_MAJOR}.${LUA_VERSION_MINOR}/)
endif()


