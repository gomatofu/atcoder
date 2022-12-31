h1,h2,h3,w1,w2,w3=map(int,input().split())
ans=0
for M11 in range(1,29):
    for M12 in range(1,29):
        for M21 in range(1,29):
            for M22 in range(1,29):
                M13=h1-(M11+M12)
                M23=h2-(M21+M22)
                M31=w1-(M11+M21)
                M32=w2-(M12+M22)
                M33=h3-(M31+M32)

                if M13 > 0 and M23 > 0 and M31 > 0 and M32 > 0 and M33 > 0:
                    if M13 + M23 + M33 == w3:
                        ans+=1

print(ans)
