# Install script for directory: /home/pi/SASDIE/MyApsIsticLuaLib

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "alpha")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}/usr/local/lib/libmyapsistic.so.0.2.0"
      "$ENV{DESTDIR}/usr/local/lib/libmyapsistic.so.0"
      "$ENV{DESTDIR}/usr/local/lib/libmyapsistic.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/libmyapsistic.so.0.2.0;/usr/local/lib/libmyapsistic.so.0;/usr/local/lib/libmyapsistic.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/usr/local/lib" TYPE SHARED_LIBRARY FILES
    "/home/pi/SASDIE/MyApsIsticLuaLib/build/alpha/libmyapsistic.so.0.2.0"
    "/home/pi/SASDIE/MyApsIsticLuaLib/build/alpha/libmyapsistic.so.0"
    "/home/pi/SASDIE/MyApsIsticLuaLib/build/alpha/libmyapsistic.so"
    )
  foreach(file
      "$ENV{DESTDIR}/usr/local/lib/libmyapsistic.so.0.2.0"
      "$ENV{DESTDIR}/usr/local/lib/libmyapsistic.so.0"
      "$ENV{DESTDIR}/usr/local/lib/libmyapsistic.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if("${CMAKE_INSTALL_COMPONENT}" STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  foreach(file
      "$ENV{DESTDIR}/usr/local/lib/lua/5.2/libmyapsistic.so.0.2.0"
      "$ENV{DESTDIR}/usr/local/lib/lua/5.2/libmyapsistic.so.0"
      "$ENV{DESTDIR}/usr/local/lib/lua/5.2/libmyapsistic.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      file(RPATH_CHECK
           FILE "${file}"
           RPATH "")
    endif()
  endforeach()
  list(APPEND CMAKE_ABSOLUTE_DESTINATION_FILES
   "/usr/local/lib/lua/5.2/libmyapsistic.so.0.2.0;/usr/local/lib/lua/5.2/libmyapsistic.so.0;/usr/local/lib/lua/5.2/libmyapsistic.so")
  if(CMAKE_WARN_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(WARNING "ABSOLUTE path INSTALL DESTINATION : ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
  if(CMAKE_ERROR_ON_ABSOLUTE_INSTALL_DESTINATION)
    message(FATAL_ERROR "ABSOLUTE path INSTALL DESTINATION forbidden (by caller): ${CMAKE_ABSOLUTE_DESTINATION_FILES}")
  endif()
file(INSTALL DESTINATION "/usr/local/lib/lua/5.2" TYPE SHARED_LIBRARY FILES
    "/home/pi/SASDIE/MyApsIsticLuaLib/build/alpha/libmyapsistic.so.0.2.0"
    "/home/pi/SASDIE/MyApsIsticLuaLib/build/alpha/libmyapsistic.so.0"
    "/home/pi/SASDIE/MyApsIsticLuaLib/build/alpha/libmyapsistic.so"
    )
  foreach(file
      "$ENV{DESTDIR}/usr/local/lib/lua/5.2/libmyapsistic.so.0.2.0"
      "$ENV{DESTDIR}/usr/local/lib/lua/5.2/libmyapsistic.so.0"
      "$ENV{DESTDIR}/usr/local/lib/lua/5.2/libmyapsistic.so"
      )
    if(EXISTS "${file}" AND
       NOT IS_SYMLINK "${file}")
      if(CMAKE_INSTALL_DO_STRIP)
        execute_process(COMMAND "/usr/bin/strip" "${file}")
      endif()
    endif()
  endforeach()
endif()

if(CMAKE_INSTALL_COMPONENT)
  set(CMAKE_INSTALL_MANIFEST "install_manifest_${CMAKE_INSTALL_COMPONENT}.txt")
else()
  set(CMAKE_INSTALL_MANIFEST "install_manifest.txt")
endif()

string(REPLACE ";" "\n" CMAKE_INSTALL_MANIFEST_CONTENT
       "${CMAKE_INSTALL_MANIFEST_FILES}")
file(WRITE "/home/pi/SASDIE/MyApsIsticLuaLib/${CMAKE_INSTALL_MANIFEST}"
     "${CMAKE_INSTALL_MANIFEST_CONTENT}")
