from metrodashboard.api.train_positions import TrainPositions
from metrodashboard.api.metro import MetroClient
from dotenv import load_dotenv

load_dotenv()
def main():
    client = MetroClient()
    positions = TrainPositions(client)
    response = positions.get_all_train_positions()
    print(response[0].train_id)
    print("Hello from metrodashboard!")


if __name__ == "__main__":
    main()
