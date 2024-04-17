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
-- __authors__ = ["davidms"]
-- __contact__ = "geology@oslandia.com"
-- __date__ = "2022/02/02"
-- __license__ = "AGPLv3"
----------------------------------------------------------------------------

-- DROP SCHEMA dem;
CREATE SCHEMA dem AUTHORIZATION postgres;

GRANT USAGE ON SCHEMA dem TO PUBLIC;

ALTER DEFAULT PRIVILEGES IN SCHEMA dem GRANT SELECT ON TABLES TO xdb_viewer;
ALTER DEFAULT PRIVILEGES IN SCHEMA dem GRANT SELECT, UPDATE, INSERT ON TABLES TO xdb_logger;
ALTER DEFAULT PRIVILEGES IN SCHEMA dem GRANT SELECT, UPDATE, INSERT ON TABLES TO xdb_importer;
ALTER DEFAULT PRIVILEGES IN SCHEMA dem GRANT ALL ON TABLES TO xdb_admin;

GRANT CREATE ON SCHEMA dem TO xdb_importer;
ALTER DEFAULT PRIVILEGES IN SCHEMA dem GRANT ALL ON TABLES TO xdb_admin;
GRANT ALL ON SCHEMA dem TO xdb_admin;