def how_much_water(water, load, clothes):
    if clothes < load:
        return "Not enough clothes"
    elif clothes > load * 2:
        return "Too much clothes"
    elif clothes == load:
        return water
    else:
        return (water * 1.1 * load) + (water * 1.1 / (clothes - load))
