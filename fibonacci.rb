sum = 2
current = 1
nextterm = 2

while nextterm < 4000000
	temp = nextterm
	nextterm = current + nextterm
	current = temp

	if nextterm % 2 == 0
		sum += nextterm
	end
end

puts sum
