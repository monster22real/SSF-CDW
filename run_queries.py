from google.cloud import bigquery


def run_query(query):
    client = bigquery.Client()
    query_job = client.query(query)
    results = query_job.result()
    return results

# Define TPC-H queries (adjust column names based on your actual schema)
queries = [
    # Query 1: Pricing Summary Report Query
    """
    SELECT
        l_returnflag,  -- Adjust this column name if needed
        l_linestatus,  -- Adjust this column name if needed
        SUM(l_quantity) AS sum_qty,
        SUM(l_extendedprice) AS sum_base_price,
        SUM(l_extendedprice * (1 - l_discount)) AS sum_disc_price,
        SUM(l_extendedprice * (1 - l_discount) * (1 + l_tax)) AS sum_charge,
        AVG(l_quantity) AS avg_qty,
        AVG(l_extendedprice) AS avg_price,
        AVG(l_discount) AS avg_disc,
        COUNT(*) AS count_order
    FROM
        `redis123.tpch_dataset.lineitem`
    GROUP BY
        l_returnflag,  -- Adjust this column name if needed
        l_linestatus  -- Adjust this column name if needed
    ORDER BY
        l_returnflag,  -- Adjust this column name if needed
        l_linestatus;  -- Adjust this column name if needed
    """,

    # Query 3: Shipping Priority Query
    """
    SELECT
        l_orderkey,
        SUM(l_extendedprice * (1 - l_discount)) AS revenue,
        o_orderdate,
        o_shippriority
    FROM
        `redis123.tpch_dataset.customer` AS c
    JOIN
        `redis123.tpch_dataset.orders` AS o
        ON c.c_custkey = o.o_custkey
    JOIN
        `redis123.tpch_dataset.lineitem` AS l
        ON l.l_orderkey = o.o_orderkey
    WHERE
        c.c_mktsegment = 'BUILDING'
        AND o.o_orderdate < DATE '1995-03-15'
    GROUP BY
        l_orderkey, o_orderdate, o_shippriority
    ORDER BY
        revenue DESC,
        o_orderdate;
    """,

    # Query 5: Local Supplier Volume Query
    """
    SELECT
        n_name,
        SUM(l_extendedprice * (1 - l_discount)) AS revenue
    FROM
        `redis123.tpch_dataset.customer` AS c
    JOIN
        `redis123.tpch_dataset.orders` AS o
        ON c.c_custkey = o.o_custkey
    JOIN
        `redis123.tpch_dataset.lineitem` AS l
        ON l.l_orderkey = o.o_orderkey
    JOIN
        `redis123.tpch_dataset.supplier` AS s
        ON l.l_suppkey = s.s_suppkey
    JOIN
        `redis123.tpch_dataset.nation` AS n
        ON c.c_nationkey = n.n_nationkey
        AND s.s_nationkey = n.n_nationkey
    WHERE
        n.n_name = 'ASIA'
        AND o.o_orderdate >= DATE '1994-01-01'
        AND o.o_orderdate < DATE '1995-01-01'
    GROUP BY
        n_name
    ORDER BY
        revenue DESC;
    """
]

# Execute and print the results of each query
for i, query in enumerate(queries):
    print(f"Running Query {i + 1}")
    result = run_query(query)
    for row in result:
        print(dict(row))
