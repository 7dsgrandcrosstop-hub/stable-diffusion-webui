# Colab T4 performance profile

This fork includes an opt-in runtime profile for SDXL on a 15 GB NVIDIA T4.
It keeps normal desktop behavior unchanged.

Enable the profile before running `launch.py` or `webui.py`:

```bash
export A1111_COLAB_T4=1
export PYTORCH_CUDA_ALLOC_CONF=max_split_size_mb:128,garbage_collection_threshold:0.8
export LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libtcmalloc_minimal.so.4
```

The profile enables these existing A1111 options by default:

- `--xformers`
- `--lowram`
- `--opt-channelslast`
- `--no-hashing`
- `--skip-version-check`

It does not enable `--medvram-sdxl`, `--lowvram`, `--no-half`, or
`--no-half-vae`. The tested 1024x1536 setup uses a full FP16 VAE and avoids
moving the UNet into Colab system RAM.

The profile also runs garbage collection after the temporary checkpoint state
dictionary is released and keeps request error logs compact. Unset
`A1111_COLAB_T4` to restore the original behavior.
