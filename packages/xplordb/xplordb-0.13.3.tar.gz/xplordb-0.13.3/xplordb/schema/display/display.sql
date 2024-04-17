----------------------------------------------------------------------------
-- xplordb
-- 
-- Copyright (C) 2022  Oslandia / OpenLog
-- This program is free software: you can redistribute it and/or modify
-- it under the terms of the GNU Affero General Public License as published
-- by the Free Software Foundation, either version 3 of the License, or
-- (at your option) any later version.
--
-- This program is distributed in the hope that it will be useful,
-- but WITHOUT ANY WARRANTY; without even the implied warranty of
-- MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
-- GNU Affero General Public License for more details.
-- 
-- You should have received a copy of the GNU Affero General Public License
-- along with this program.  If not, see <https://www.gnu.org/licenses/>.
-- 
-- __authors__ = ["vlarmet"]
-- __contact__ = "vincent.larmet@apeiron.technology"
-- __date__ = "2024/03/18"
-- __license__ = "AGPLv3"
----------------------------------------------------------------------------

-- DROP SCHEMA dh;
CREATE SCHEMA display AUTHORIZATION postgres;

GRANT USAGE ON SCHEMA display TO PUBLIC;

ALTER DEFAULT PRIVILEGES IN SCHEMA display GRANT SELECT ON TABLES TO xdb_viewer;
ALTER DEFAULT PRIVILEGES IN SCHEMA display GRANT SELECT, UPDATE, INSERT ON TABLES TO xdb_logger;
ALTER DEFAULT PRIVILEGES IN SCHEMA display GRANT SELECT, UPDATE, INSERT ON TABLES TO xdb_importer;
ALTER DEFAULT PRIVILEGES IN SCHEMA display GRANT ALL ON TABLES TO xdb_admin;

GRANT CREATE ON SCHEMA display TO xdb_importer;
GRANT CREATE ON SCHEMA display TO xdb_viewer;
GRANT ALL ON SCHEMA display TO xdb_admin;