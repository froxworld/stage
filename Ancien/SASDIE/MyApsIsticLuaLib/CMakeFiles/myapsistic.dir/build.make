# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.7

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /home/pi/SASDIE/MyApsIsticLuaLib

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /home/pi/SASDIE/MyApsIsticLuaLib

# Include any dependencies generated for this target.
include CMakeFiles/myapsistic.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/myapsistic.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/myapsistic.dir/flags.make

CMakeFiles/myapsistic.dir/src/services.c.o: CMakeFiles/myapsistic.dir/flags.make
CMakeFiles/myapsistic.dir/src/services.c.o: src/services.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/SASDIE/MyApsIsticLuaLib/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building C object CMakeFiles/myapsistic.dir/src/services.c.o"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/myapsistic.dir/src/services.c.o   -c /home/pi/SASDIE/MyApsIsticLuaLib/src/services.c

CMakeFiles/myapsistic.dir/src/services.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/myapsistic.dir/src/services.c.i"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/pi/SASDIE/MyApsIsticLuaLib/src/services.c > CMakeFiles/myapsistic.dir/src/services.c.i

CMakeFiles/myapsistic.dir/src/services.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/myapsistic.dir/src/services.c.s"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/pi/SASDIE/MyApsIsticLuaLib/src/services.c -o CMakeFiles/myapsistic.dir/src/services.c.s

CMakeFiles/myapsistic.dir/src/services.c.o.requires:

.PHONY : CMakeFiles/myapsistic.dir/src/services.c.o.requires

CMakeFiles/myapsistic.dir/src/services.c.o.provides: CMakeFiles/myapsistic.dir/src/services.c.o.requires
	$(MAKE) -f CMakeFiles/myapsistic.dir/build.make CMakeFiles/myapsistic.dir/src/services.c.o.provides.build
.PHONY : CMakeFiles/myapsistic.dir/src/services.c.o.provides

CMakeFiles/myapsistic.dir/src/services.c.o.provides.build: CMakeFiles/myapsistic.dir/src/services.c.o


CMakeFiles/myapsistic.dir/src/jsmn.c.o: CMakeFiles/myapsistic.dir/flags.make
CMakeFiles/myapsistic.dir/src/jsmn.c.o: src/jsmn.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/SASDIE/MyApsIsticLuaLib/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/myapsistic.dir/src/jsmn.c.o"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/myapsistic.dir/src/jsmn.c.o   -c /home/pi/SASDIE/MyApsIsticLuaLib/src/jsmn.c

CMakeFiles/myapsistic.dir/src/jsmn.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/myapsistic.dir/src/jsmn.c.i"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/pi/SASDIE/MyApsIsticLuaLib/src/jsmn.c > CMakeFiles/myapsistic.dir/src/jsmn.c.i

CMakeFiles/myapsistic.dir/src/jsmn.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/myapsistic.dir/src/jsmn.c.s"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/pi/SASDIE/MyApsIsticLuaLib/src/jsmn.c -o CMakeFiles/myapsistic.dir/src/jsmn.c.s

CMakeFiles/myapsistic.dir/src/jsmn.c.o.requires:

.PHONY : CMakeFiles/myapsistic.dir/src/jsmn.c.o.requires

CMakeFiles/myapsistic.dir/src/jsmn.c.o.provides: CMakeFiles/myapsistic.dir/src/jsmn.c.o.requires
	$(MAKE) -f CMakeFiles/myapsistic.dir/build.make CMakeFiles/myapsistic.dir/src/jsmn.c.o.provides.build
.PHONY : CMakeFiles/myapsistic.dir/src/jsmn.c.o.provides

CMakeFiles/myapsistic.dir/src/jsmn.c.o.provides.build: CMakeFiles/myapsistic.dir/src/jsmn.c.o


CMakeFiles/myapsistic.dir/src/network.c.o: CMakeFiles/myapsistic.dir/flags.make
CMakeFiles/myapsistic.dir/src/network.c.o: src/network.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/SASDIE/MyApsIsticLuaLib/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Building C object CMakeFiles/myapsistic.dir/src/network.c.o"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/myapsistic.dir/src/network.c.o   -c /home/pi/SASDIE/MyApsIsticLuaLib/src/network.c

CMakeFiles/myapsistic.dir/src/network.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/myapsistic.dir/src/network.c.i"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/pi/SASDIE/MyApsIsticLuaLib/src/network.c > CMakeFiles/myapsistic.dir/src/network.c.i

CMakeFiles/myapsistic.dir/src/network.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/myapsistic.dir/src/network.c.s"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/pi/SASDIE/MyApsIsticLuaLib/src/network.c -o CMakeFiles/myapsistic.dir/src/network.c.s

CMakeFiles/myapsistic.dir/src/network.c.o.requires:

.PHONY : CMakeFiles/myapsistic.dir/src/network.c.o.requires

CMakeFiles/myapsistic.dir/src/network.c.o.provides: CMakeFiles/myapsistic.dir/src/network.c.o.requires
	$(MAKE) -f CMakeFiles/myapsistic.dir/build.make CMakeFiles/myapsistic.dir/src/network.c.o.provides.build
.PHONY : CMakeFiles/myapsistic.dir/src/network.c.o.provides

CMakeFiles/myapsistic.dir/src/network.c.o.provides.build: CMakeFiles/myapsistic.dir/src/network.c.o


CMakeFiles/myapsistic.dir/src/lua_bindings.c.o: CMakeFiles/myapsistic.dir/flags.make
CMakeFiles/myapsistic.dir/src/lua_bindings.c.o: src/lua_bindings.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/home/pi/SASDIE/MyApsIsticLuaLib/CMakeFiles --progress-num=$(CMAKE_PROGRESS_4) "Building C object CMakeFiles/myapsistic.dir/src/lua_bindings.c.o"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/myapsistic.dir/src/lua_bindings.c.o   -c /home/pi/SASDIE/MyApsIsticLuaLib/src/lua_bindings.c

CMakeFiles/myapsistic.dir/src/lua_bindings.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/myapsistic.dir/src/lua_bindings.c.i"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /home/pi/SASDIE/MyApsIsticLuaLib/src/lua_bindings.c > CMakeFiles/myapsistic.dir/src/lua_bindings.c.i

CMakeFiles/myapsistic.dir/src/lua_bindings.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/myapsistic.dir/src/lua_bindings.c.s"
	/usr/bin/cc  $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /home/pi/SASDIE/MyApsIsticLuaLib/src/lua_bindings.c -o CMakeFiles/myapsistic.dir/src/lua_bindings.c.s

CMakeFiles/myapsistic.dir/src/lua_bindings.c.o.requires:

.PHONY : CMakeFiles/myapsistic.dir/src/lua_bindings.c.o.requires

CMakeFiles/myapsistic.dir/src/lua_bindings.c.o.provides: CMakeFiles/myapsistic.dir/src/lua_bindings.c.o.requires
	$(MAKE) -f CMakeFiles/myapsistic.dir/build.make CMakeFiles/myapsistic.dir/src/lua_bindings.c.o.provides.build
.PHONY : CMakeFiles/myapsistic.dir/src/lua_bindings.c.o.provides

CMakeFiles/myapsistic.dir/src/lua_bindings.c.o.provides.build: CMakeFiles/myapsistic.dir/src/lua_bindings.c.o


# Object files for target myapsistic
myapsistic_OBJECTS = \
"CMakeFiles/myapsistic.dir/src/services.c.o" \
"CMakeFiles/myapsistic.dir/src/jsmn.c.o" \
"CMakeFiles/myapsistic.dir/src/network.c.o" \
"CMakeFiles/myapsistic.dir/src/lua_bindings.c.o"

# External object files for target myapsistic
myapsistic_EXTERNAL_OBJECTS =

build/alpha/libmyapsistic.so.0.2.0: CMakeFiles/myapsistic.dir/src/services.c.o
build/alpha/libmyapsistic.so.0.2.0: CMakeFiles/myapsistic.dir/src/jsmn.c.o
build/alpha/libmyapsistic.so.0.2.0: CMakeFiles/myapsistic.dir/src/network.c.o
build/alpha/libmyapsistic.so.0.2.0: CMakeFiles/myapsistic.dir/src/lua_bindings.c.o
build/alpha/libmyapsistic.so.0.2.0: CMakeFiles/myapsistic.dir/build.make
build/alpha/libmyapsistic.so.0.2.0: /usr/lib/arm-linux-gnueabihf/libcurl.so
build/alpha/libmyapsistic.so.0.2.0: CMakeFiles/myapsistic.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/home/pi/SASDIE/MyApsIsticLuaLib/CMakeFiles --progress-num=$(CMAKE_PROGRESS_5) "Linking C shared library build/alpha/libmyapsistic.so"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/myapsistic.dir/link.txt --verbose=$(VERBOSE)
	$(CMAKE_COMMAND) -E cmake_symlink_library build/alpha/libmyapsistic.so.0.2.0 build/alpha/libmyapsistic.so.0 build/alpha/libmyapsistic.so

build/alpha/libmyapsistic.so.0: build/alpha/libmyapsistic.so.0.2.0
	@$(CMAKE_COMMAND) -E touch_nocreate build/alpha/libmyapsistic.so.0

build/alpha/libmyapsistic.so: build/alpha/libmyapsistic.so.0.2.0
	@$(CMAKE_COMMAND) -E touch_nocreate build/alpha/libmyapsistic.so

# Rule to build all files generated by this target.
CMakeFiles/myapsistic.dir/build: build/alpha/libmyapsistic.so

.PHONY : CMakeFiles/myapsistic.dir/build

CMakeFiles/myapsistic.dir/requires: CMakeFiles/myapsistic.dir/src/services.c.o.requires
CMakeFiles/myapsistic.dir/requires: CMakeFiles/myapsistic.dir/src/jsmn.c.o.requires
CMakeFiles/myapsistic.dir/requires: CMakeFiles/myapsistic.dir/src/network.c.o.requires
CMakeFiles/myapsistic.dir/requires: CMakeFiles/myapsistic.dir/src/lua_bindings.c.o.requires

.PHONY : CMakeFiles/myapsistic.dir/requires

CMakeFiles/myapsistic.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/myapsistic.dir/cmake_clean.cmake
.PHONY : CMakeFiles/myapsistic.dir/clean

CMakeFiles/myapsistic.dir/depend:
	cd /home/pi/SASDIE/MyApsIsticLuaLib && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /home/pi/SASDIE/MyApsIsticLuaLib /home/pi/SASDIE/MyApsIsticLuaLib /home/pi/SASDIE/MyApsIsticLuaLib /home/pi/SASDIE/MyApsIsticLuaLib /home/pi/SASDIE/MyApsIsticLuaLib/CMakeFiles/myapsistic.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/myapsistic.dir/depend

