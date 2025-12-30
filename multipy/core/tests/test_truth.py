import multipy as mp


def main() -> None:
   truth = mp.truth_scope((1, 20), (1, 30))
   for t in truth:
       print(t)

if __name__ == "__main__":
    main()
