import argparse
import pandas as pd
import random

def generate_microsatellites(repeat_size, num_microsatellites):
    """
    Generate synthetic microsatellites of a specific repeat size
    """
    microsatellites = []
    for i in range(num_microsatellites):
        repeat_unit = ''.join([random.choice(['A', 'C', 'T', 'G']) for _ in range(repeat_size)])
        repeat_number = random.randint(5, 15)
        microsatellites.append(repeat_unit * repeat_number)
    return microsatellites

parser = argparse.ArgumentParser(description='Generate synthetic microsatellites')
parser.add_argument('--repeat_size', type=int, required=True, help='The size of the repeat unit')
parser.add_argument('--num_microsatellites', type=int, required=True, help='The number of microsatellites to generate')
parser.add_argument('--output_file', type=str, default='microsatellites.csv', help='The output file name')

args = parser.parse_args()

# Generate synthetic microsatellites
microsatellites = generate_microsatellites(args.repeat_size, args.num_microsatellites)

# Add repeat size labels
repeat_sizes = [args.repeat_size] * args.num_microsatellites

# Create dataframe from microsatellites and repeat sizes
df = pd.DataFrame({'Sequence': microsatellites, 'Repeat Size': repeat_sizes})

# Generate random front and back sequences
front_sequences = []
back_sequences = []
for i in range(args.num_microsatellites):
    random_front_length = random.randint(50, 150)
    random_back_length = random.randint(50, 150)
    random_front = ''.join([random.choice(['A', 'C', 'T', 'G']) for _ in range(random_front_length)])
    random_back = ''.join([random.choice(['A', 'C', 'T', 'G']) for _ in range(random_back_length)])
    front_sequences.append(random_front)
    back_sequences.append(random_back)

# Add full sequences to dataframe
df['Full Sequence'] = pd.Series(front_sequences) + df['Sequence'] + pd.Series(back_sequences)

# Save dataframe to CSV file
df_new = df[['Full Sequence', 'Repeat Size']]
df_new.to_csv(args.output_file, index=False)
