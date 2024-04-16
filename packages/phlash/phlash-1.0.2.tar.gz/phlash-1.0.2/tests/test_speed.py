import numpy as np
from pytest import fixture
import jax
from jax import jit, grad, jacfwd, jacrev, vmap

from phlash.hmm import psmc_ll
from phlash.kernel import get_kernel

@fixture(params=[100, 200, 500, 1000])
def batch_size(request):
    return request.param

@fixture
def bench_data(rng, batch_size):
    return (rng.uniform(size=(batch_size, 100_000)) < 0.05).astype(np.int8)

@fixture
def bench_kern(bench_data):
    return get_kernel(M=16, data=bench_data, double_precision=False)

def test_gpu_speed(benchmark, batch_size, dm, bench_kern):
    inds = np.arange(batch_size)
    f = jit(vmap(grad(bench_kern.loglik), in_axes=(None, 0)))
    res = f(dm, inds)
    jax.block_until_ready(res)
    benchmark(f, dm, inds)

def test_jax_fwd_speed(benchmark, bench_data, dm):
    f = jit(vmap(jacfwd(psmc_ll), in_axes=(None, 0)))
    res = f(dm, bench_data)
    jax.block_until_ready(res)
    benchmark(f, dm, bench_data)

def test_jax_rev_speed(benchmark, bench_data, dm):
    f = jit(vmap(jacrev(psmc_ll), in_axes=(None, 0)))
    res = f(dm, bench_data)
    jax.block_until_ready(res)
    benchmark(f, dm, bench_data)
