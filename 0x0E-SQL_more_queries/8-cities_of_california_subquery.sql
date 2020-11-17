-- This script lists all the cities of California that can be found in database
-- hbtn_0d_usa

SELECT
    id,
    name
    FROM
        hbtn_0d_usa.cities
    WHERE
        state_id=(
            SELECT
                id
                FROM
                    hbtn_0d_usa.states
                WHERE
                    name='California'
        ) ORDER BY id;
