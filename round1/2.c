#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/mman.h>
#include <sys/types.h>
#include <sys/stat.h>

#define TRIE_SIZE 26 * 200000 * sizeof(long)
#define LOCATION(x) (((long)x)/4) & ((1 << 13) - 1)

int main(int argc, char** argv) {
	int fd = open("autocomplete2.txt", O_RDONLY);
	struct stat sbuf;
	stat("autocomplete2.txt", &sbuf);
	char* data = mmap((caddr_t)0, sbuf.st_size, PROT_READ, MAP_SHARED, fd, 0);
	
	int num_iterations = atoi(data);
	// printf("%d\n", num_iterations);
	while (*data != '\n') {
		data++;
	}
	data++;

	long* trie_root = (long*)malloc(TRIE_SIZE);
	if (trie_root == NULL) {
		printf("malloc failed.\n");
		exit(1);
	}

	int iteration;
	for (iteration = 1; iteration <= num_iterations; iteration++) {
		// printf("%d\n", iteration);
		int num_words = atoi(data);
		while (*data != '\n') {
			data++;
		}
		data++;
		memset(trie_root, 0, TRIE_SIZE);

		char* start = data - 1;
		long frontier = 26;
		long total = 0;
		while (num_words > 0) {
			long* node = trie_root;
			num_words--;
			while (1) {
				char character = *data;
				if (character == '\n') {
					data++;
					break;
				}
				// printf("%c\n", character);
				total += 1;
				character -= 'a';

				long* spot = node + (unsigned long)character;
				// printf("%ld\n", (long)(spot - trie_root));
				long value = *spot;
				if (value > 0) {
					node = trie_root + value;
					data++;
					// printf("list %ld %d\n", LOCATION(spot), value);
					continue;
				}
				if (value == 0) {
					*spot = start - data - 1;
					while (*(++data) != '\n') {
						// printf("%c", *data);
					};
					// printf("\n");
					data++;
					break;
				}
				// printf("else %ld %d\n", LOCATION(spot), frontier);
				*spot = frontier;
				node = trie_root + frontier;
				frontier += 26;
				// printf("%d\n", frontier/26);
				char* word = start - value;
				character = *word;
				if (character != '\n') {
					long* location = node + (unsigned long)character - 'a';
					*location = value - 1;
					// printf("  -> %ld %c %ld %d\n", LOCATION(node), character, LOCATION(location), value - 1);
				}
				data++;
				// printf("...\n");
			}
			// printf("Total: %d %d %d %d\n", total, data - start + 1, *(data-2), *(data-1));
		}
		printf("Case #%d: %ld\n", iteration, total);
	}
}
