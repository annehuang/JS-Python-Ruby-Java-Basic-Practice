largest = 0 
for i in 100...999 do
	for j in 100...999 do
		product = i * j

		if product.to_s == product.to_s.reverse
			palindrome = product
			if palindrome > largest
				largest = palindrome
			end
		end
	end
end

puts largest
