static void binaryprint_le(uint8_t * binaryBuf, const uint8_t * data, size_t size)
{
// write in Little Endian order
 	while (size--){
   		*binaryBuf = *(data + size);
		printf("%02hhX", *binaryBuf);
   		binaryBuf++;
 	}

  	printf("\n");
}
