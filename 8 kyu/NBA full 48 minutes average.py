def nba_extrap(ppg, mpg):
    FULL_GAME = 48
    if mpg != 0:
        coefficient = FULL_GAME / mpg
        ppg = ppg * coefficient
        if ppg != 0:
            return round(ppg, 1)
    else:
        return 0
