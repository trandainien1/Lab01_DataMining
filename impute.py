from utils import *

def impute(df, column_names, method):
  missing_col_names = extract_columns_with_missing_value(df) 

  for name in column_names:
    new_cols = []
    impute_value = 0

    if column_with_all_missing_values(df, name):
      df[name] = [''] * len(df[name]) 
      continue
    
    if not type(df[name][0]) == str:
      if method == 'mean':
        impute_value = get_mean_of_a_column(df, name)
      else:
        impute_value = get_median_of_a_column(df, name) 
   
    else:
      impute_value = get_mode_of_a_column(df, name)

    for value in df[name]:
      if value is None or value == '':
        value = impute_value
      new_cols.append(value)

    df[name] = new_cols

  return df

# Command line Processing

argParser = argparse.ArgumentParser(description='Impute process')
argParser.add_argument('in', help='input file name')
argParser.add_argument("-method", "--method", help="method(mean or median)")
argParser.add_argument("-columns", "--columns", default=[], nargs='*', help="columns you want to impute, leave it empty for impute all the columns if necessary")
argParser.add_argument("-out", "--out", help="output file name")

args = argParser.parse_args()

input_file = sys.argv[1]

df = get_data(input_file)

df = convert_column_types(df)

method = args.method
columns = args.columns
output_file = args.out 

new_df = impute(df, columns, method)

write_data(new_df, output_file)


