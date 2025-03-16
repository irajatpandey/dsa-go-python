def is_evenly_divisible(n):
   if n % 2 == 0 and n > 2:
      return True
   else:
      return False


if __name__ == "__main__":
    n = int(input())    
    ans = is_evenly_divisible(n)
    if ans:
        print("YES")
    else:
        print("NO")
