from rich.console import Console
from rich.table import Table
from typing import Tuple

# Constant for petrol price
PETROL_PRICE_PER_LITRE = 1.69

def get_user_input() -> Tuple[str, float, float]:
    """
    Get user input for car model name, distance travelled, and amount paid for fuel.

    Returns:
        Tuple[str, float, float]: A tuple containing the car model name, distance travelled in km, and amount paid in AUD.
    """
    model_name = input("Enter your car model name: ")
    distance_travelled = float(input("Enter distance travelled in km: "))
    amount_paid = float(input("Enter the dollar value of fuel bought for the trip (AUD): "))
    return model_name, distance_travelled, amount_paid

def calculate_efficiency(distance_travelled: float, amount_paid: float, petrol_price_per_litre: float) -> Tuple[float, float]:
    """
    Calculate the fuel efficiency of the car.

    Args:
        distance_travelled (float): Distance travelled in kilometers.
        amount_paid (float): Amount paid for fuel in AUD.
        petrol_price_per_litre (float): Price of petrol per litre in AUD.

    Returns:
        Tuple[float, float]: A tuple containing the efficiency in litres per 100 km and km per litre.
    """
    fuel_consumed = amount_paid / petrol_price_per_litre
    efficiency_l_per_100_km = (fuel_consumed / distance_travelled) * 100
    efficiency_km_per_l = distance_travelled / fuel_consumed
    return efficiency_l_per_100_km, efficiency_km_per_l

def display_efficiency(model_name: str, efficiency_l_per_100_km: float, efficiency_km_per_l: float) -> None:
    """
    Display the fuel efficiency results in a formatted table.

    Args:
        model_name (str): The car model name.
        efficiency_l_per_100_km (float): Efficiency in litres per 100 km.
        efficiency_km_per_l (float): Efficiency in km per litre.
    """
    console = Console()
    table = Table(title=f"Fuel Efficiency for {model_name}")

    table.add_column("Description", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", justify="right", style="magenta")

    table.add_row("Efficiency (L/100 km):", f"{efficiency_l_per_100_km:.2f}")
    table.add_row("Efficiency (km/L):", f"{efficiency_km_per_l:.2f}")

    console.print(table)
    console.print("\nThanks for using the program.")

def main() -> None:
    """
    Main function to run the fuel efficiency calculator program.
    """
    console = Console()
    console.print("*** Welcome to the fuel efficiency calculator! ***\n", style="bold green")

    model_name, distance_travelled, amount_paid = get_user_input()
    efficiency_l_per_100_km, efficiency_km_per_l = calculate_efficiency(distance_travelled, amount_paid, PETROL_PRICE_PER_LITRE)
    display_efficiency(model_name, efficiency_l_per_100_km, efficiency_km_per_l)

if __name__ == "__main__":
    main()
