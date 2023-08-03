star2movies = {}
n = int(input())
for i in range(n):
    title, star1, star2 = input().split(",")
    title = title.strip(); star1 = star1.strip(); star2 = star2.strip()
    if star1 not in star2movies:
        star2movies[star1] = [title]
    else:
        star2movies[star1].append(title)
    if star2 not in star2movies:
        star2movies[star2] = [title]
    else:
        star2movies[star2].append(title)
        
        
        
        
stars = [e.strip() for e in input().split(",")] # read the last input line 
for star in stars:
    if star in star2movies:
        print(star, "->", ", ".join(star2movies[star]))
    else:
        print(star, "->", "Not found")
        
        
# 9
# Rush Hour, Jackie Chan, Chris Tucker
# Shanghai Noon, Jackie Chan, Owen Wilson 
# Shanghai Knights, Jackie Chan, Owen Wilson
# The Medallion, Jackie Chan, Lee Evans
# Wedding Crashers, Owen Wilson, Vince Vaughn 
# Midnight in Paris, Owen Wilson, Rachel McAdams 
# Mousehunt, Nathan Lane, Lee Evans
# The Forbidden Kingdom, Jackie Chan, Jet Li
# The One, Jet Li, Jason Statham
# Jet Li, Lee Evans, Tony Jaa
# print(star2movies)