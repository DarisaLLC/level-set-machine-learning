# Perform out of bounds on indices (0=False, 1=True)
CHECK_INDICES=0

masked_grad:
	gcc -DMI_CHECK_INDEX=$(CHECK_INDICES) -std=c99 -O3 \
		-shared -o _radii_from_mask.so _radii_from_mask.c

clean:
	rm -f *.so
