all: overrun overlab overfixed


overrun: overrun.c
	gcc --debug -U_FORTIFY_SOURCE -fno-stack-protector overrun.c -o overrun

overlab: overlab.c
	gcc --debug -U_FORTIFY_SOURCE -fno-stack-protector overrun.c -o overlab

overfixed: overfixed.c
	gcc --debug -U_FORTIFY_SOURCE -fno-stack-protector overrun.c -o overfixed

clean:
	rm overrun overlab overfixed
