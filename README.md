# OFSMVRP
Solution for the Open Fleet Size and Mix Vehicle Routing Problem.

### 🧩 What is the Open Fleet Size and Mix Vehicle Routing Problem?

The **Open Fleet Size and Mix Vehicle Routing Problem (OFSMVRP)** is a variant of the classic Vehicle Routing Problem (VRP). 

It focuses on determining:

- **The optimal number of vehicles to use** (fleet size),
- **Which types of vehicles to select** (fleet mix),
- **And the best routes** for those vehicles to deliver goods to a set of customers.

Unlike traditional VRPs where the fleet is fixed and returns to the depot, the **"open"** version means that vehicles **do not need to return to the depot** after completing their deliveries.

#### 🔑 Key characteristics:
- The fleet is **not predetermined** — you can choose from different vehicle types with varying costs and capacities.
- Each vehicle starts from the depot but **ends its route at the last customer**.
- The **total cost** depends on:
  - The **distance (in kilometers)** traveled by each vehicle,
  - The **type of vehicle** used for each route (since each vehicle type has a different cost per kilometer).
- The objective is to **minimize the overall cost**, balancing the number of vehicles, their types, and the routing distances.

This problem is highly relevant in transportation and logistics, especially when companies must decide how to efficiently deliver goods using a flexible fleet.
