total = 0
for item in "$*"; do
    total=$((total + 1))
done

if [$# -eq 3 ]; then
    total=$((total + 20))
fi

["$1" = "srv01"]
echo "$total-$#-$?"
