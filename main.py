from suite import NotreSuite

if __name__ == '__main__':
    u = NotreSuite()
    for i in range(2023):
            u.compute_next()

    print(u.get_values())
    print(f"Il y a {u.sort_and_count()[0]} fois u = 0 et {u.sort_and_count()[1]} fois u = 1")
    print(f"Les autres valeurs de u sont : {u.sort_and_count()[2]}")