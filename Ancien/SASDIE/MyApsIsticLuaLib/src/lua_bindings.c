/* MyApsIsticLuaLib
 * Copyright © 2016 François Bodin
 *
 * This library is free software; you can redistribute it and/or
 * modify it under the terms of the GNU Lesser General Public
 * License as published by the Free Software Foundation; either
 * version 3 of the License, or (at your option) any later version.
 *
 * This library is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
 * Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public
 * License along with this library. If not, see <http://www.gnu.org/licenses/>.
 */
#include "common.h"

//for yield function
#include <sched.h>
#include <lua.h>
#include <lualib.h>
#include <lauxlib.h>

//for the network functions
#ifdef WITH_NETWORK
#include "network.h"
#endif

/*define functions used by lua or luaL_Reg*/
static const luaL_Reg myapslib[] = {
#ifdef WITH_NETWORK
  {"connect", myapsisticlualib_connect},
  {"disconnect", myapsisticlualib_disconnect},
  {"adduser", addUser},
  {"rmuser", rmUser},
  {"generate",addOutput},
  {"getfile",getFile},
  {"putfile",putAFile},
  {"getmetadata",getFileMetaData},
  {"putmetadata",putFileMetaData},
  {"rmmetadata",rmFileMetaData},
  {"gettask",getTask},
  {"puttask",putTask},
  {"listoffiles",listOfFiles},
  {"xlistoffiles",extendedListOfFiles},
  {"addmenu",addMenu},
  {"addactions",addActions},
  {"chgpasswd",chgPasswd},
  {"position",getPosition},
  {"getkeyid",getKeyid},
#endif
	{NULL, NULL}
};

MYAPS_EXPORT int luaopen_libmyapsistic(lua_State *L){
#if LUA_VERSION_NUM <= 501
  luaL_register(L, "myapslib", myapslib);
#else
  lua_newtable(L);
  luaL_setfuncs(L, myapslib, 0);
#endif
  return 1;
}
