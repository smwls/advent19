#include <stdio.h>
#include <stdbool.h>

int compare_pair(int a, int b) {
	if (a < b) {
		return 1;
	} else if (a > b) {
		return -1;
	} else {
		return 0;
	}
}

void print_array(int *arr1, int len) {
	printf("%s", "[");
	for (int i = 0; i < len - 1; i++) {
		printf("%d, ", arr1[i]);
	}
	printf("%d]\n", arr1[len - 1]);
}

bool is_equal(int arr1[12], int arr2[12], int axis) {
	for (int i = 0; i < 4; i++) {
		if (arr1[axis + i*3] != arr2[axis + i*3]) {
			return false;
		}
	}
	return true;
}

void update(int positions[12], int velocities[12], int dim) {
	for (int moon_1 = 0; moon_1 < 4; moon_1++) {
		for (int moon_2 = 0; moon_2 < 4; moon_2++) {
			velocities[moon_1*3 + dim] += compare_pair(positions[moon_1*3 + dim], positions[moon_2*3 + dim]); 
		}
	}

	for (int row = 0; row < 4; row++) {
		positions[row*3 + dim] += velocities[row*3 + dim];
	}
}

void set_eq(int old[12], int new[12]) {
	for (int i = 0; i < 12; i++) {
		old[i] = new[i];
	}
}

void brent() {
	int positions_1[12] = {7,10,17, -2,7,0,12,5,12,5,-8,6};
	int positions_2[12] = {7,10,17, -2,7,0,12,5,12,5,-8,6};
	int velocities_1[12] = {0,0,0,0,0,0,0,0,0,0,0,0};
	int velocities_2[12] = {0,0,0,0,0,0,0,0,0,0,0,0};

	int start_pos[12] = {7,10,17, -2,7,0,12,5,12,5,-8,6};
	int start_vel[12] = {0,0,0,0,0,0,0,0,0,0,0,0};

	int periods[3] = {0,0,0};
	int mus[3] = {0,0,0};

	for (int axis = 0; axis < 3; axis++) {
		update(positions_2, velocities_2, axis);
		unsigned long long int power = 1;
		unsigned long long int lam = 1;
		unsigned long long int mu = 0;
		unsigned long long int iter = 0;
		while (!(is_equal(positions_1, positions_2, axis) && is_equal(velocities_1, velocities_2, axis))) {
			if (power == lam) {
				set_eq(positions_1, positions_2);
				set_eq(velocities_1, velocities_2);
				power *= 2;
				lam = 0;
			}
			update(positions_2, velocities_2, axis);
			lam += 1;
			iter += 1;
		}

		set_eq(positions_1, start_pos);
		set_eq(velocities_1, start_vel);

		set_eq(positions_2, start_pos);
		set_eq(velocities_2, start_vel);

		for (unsigned long long int i = 0; i < lam; i++) {
			update(positions_2, velocities_2, axis);
		}

		while (!(is_equal(positions_1, positions_2, axis) && is_equal(velocities_1, velocities_2, axis))) {
			update(positions_1, velocities_1, axis);
			update(positions_2, velocities_2, axis);
			mu += 1;
		}
		periods[axis] = lam;
	}
	print_array(periods, 3);
}
int main(int argc, char** argv) {
	brent();
}


