largest = 0 # Identify largest palindrome that is the product of 2 3-digit numbers

for i in 100...999 do
	for j in 100...999 do
		product = i * j

		if product.to_s == product.to_s.reverse
			palindrome = product
			if palindrome > largest # If this is the largest palindrome found so far
				largest = palindrome
			end
		end
	end
end

puts largest # print largest palindrome
