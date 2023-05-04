import auger
import triangle as module

def main():
  p = module.triangle(0, 1, 2)
  print(p)

if __name__ == "__main__":
  with auger.magic([module]):   # this is the new line and invokes Auger
    main()