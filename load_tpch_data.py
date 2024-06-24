import pandas as pd

# Define file paths
customer_file = 'customer.tbl'
orders_file = 'orders.tbl'
lineitem_file = 'lineitem.tbl'
supplier_file = 'supplier.tbl'
part_file = 'part.tbl'
partsupp_file = 'partsupp.tbl'
nation_file = 'nation.tbl'
region_file = 'region.tbl'

# Load data into DataFrames
customer_df = pd.read_csv(customer_file, delimiter='|', header=None, names=['c_custkey', 'c_name', 'c_address', 'c_nationkey', 'c_phone', 'c_acctbal', 'c_mktsegment', 'c_comment'])
orders_df = pd.read_csv(orders_file, delimiter='|', header=None, names=['o_orderkey', 'o_custkey', 'o_orderstatus', 'o_totalprice', 'o_orderdate', 'o_orderpriority', 'o_clerk', 'o_shippriority', 'o_comment'])
lineitem_df = pd.read_csv(lineitem_file, delimiter='|', header=None, names=['l_orderkey', 'l_partkey', 'l_suppkey', 'l_linenumber', 'l_quantity', 'l_extendedprice', 'l_discount', 'l_tax', 'l_returnflag', 'l_linestatus', 'l_shipdate', 'l_commitdate', 'l_receiptdate', 'l_shipinstruct', 'l_shipmode', 'l_comment'])
supplier_df = pd.read_csv(supplier_file, delimiter='|', header=None, names=['s_suppkey', 's_name', 's_address', 's_nationkey', 's_phone', 's_acctbal', 's_comment'])
part_df = pd.read_csv(part_file, delimiter='|', header=None, names=['p_partkey', 'p_name', 'p_mfgr', 'p_brand', 'p_type', 'p_size', 'p_container', 'p_retailprice', 'p_comment'])
partsupp_df = pd.read_csv(partsupp_file, delimiter='|', header=None, names=['ps_partkey', 'ps_suppkey', 'ps_availqty', 'ps_supplycost', 'ps_comment'])
nation_df = pd.read_csv(nation_file, delimiter='|', header=None, names=['n_nationkey', 'n_name', 'n_regionkey', 'n_comment'])
region_df = pd.read_csv(region_file, delimiter='|', header=None, names=['r_regionkey', 'r_name', 'r_comment'])

# Print DataFrame info to verify
print(customer_df.head())
print(orders_df.head())
print(lineitem_df.head())
print(supplier_df.head())
print(part_df.head())
print(partsupp_df.head())
print(nation_df.head())
print(region_df.head())
