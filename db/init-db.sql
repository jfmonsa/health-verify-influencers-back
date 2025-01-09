-- Works just like: CREATE DATABASE IF NOT EXISTS <db_name>;
SELECT 'CREATE DATABASE health_influencers'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'health_influencers')\gexec