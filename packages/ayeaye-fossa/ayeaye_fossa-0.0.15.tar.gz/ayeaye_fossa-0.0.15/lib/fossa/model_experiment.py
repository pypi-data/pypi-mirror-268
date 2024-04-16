from ayeaye import connector_resolver
from examples.example_etl import SecondTimeLucky


if __name__ == "__main__":
    with connector_resolver.context(output_datasets="/Users/si/Documents/Scratch/test_docs"):
        m = SecondTimeLucky()
        m.go()
