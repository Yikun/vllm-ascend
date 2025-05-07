# Feature Support

The feature support principle of vLLM Ascend is: **aligned with the vLLM**. We are also actively collaborating with the community to accelerate support.

```{note}
vLLM V1 Engine is experimentally supportted in v0.7.3, and will get a functional support in next v0.8 release.
```

| Feature                       | vLLM Ascend    | MindIE Turbo    | Notes                                                                  |
|-------------------------------|----------------|-----------------|------------------------------------------------------------------------|
| Chunked Prefill               | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Automatic Prefix Caching      | 🟢 Functional  | 🟢 Functional  | [Usage Limits](https://github.com/vllm-project/vllm-ascend/issues/732) |
| LoRA                          | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Prompt adapter                | 🔴 NO plan     | 🔴 NO plan     | /                                                                      |
| Speculative decoding          | 🟢 Functional  | 🟢 Functional  | [Usage Limits](https://github.com/vllm-project/vllm-ascend/issues/734) |
| Pooling                       | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Enc-dec                       | 🔴 NO plan     | 🔴 NO plan     | /                                                                      |
| Multi Modality                | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| LogProbs                      | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Prompt logProbs               | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Async output                  | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Multi step scheduler          | 🟢 Functional  | 🟢 Functional  | /                                                                      | 
| Best of                       | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Beam search                   | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Guided Decoding               | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Tensor Parallel               | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Pipeline Parallel             | 🟢 Functional  | 🟢 Functional  | /                                                                      |
| Expert Parallel               | 🔴 NO plan     | 🔴 NO plan     | /                                                                      |
| Data Parallel                 | 🔴 NO plan     | 🔴 NO plan     | /                                                                      |
| Prefill Decode Disaggregation | 🟢 Functional  | 🟢 Functional  | todo                                                                   |
| Quantization                  | 🔴 NO plan     | 🟢 Functional  | todo                                                                   |
| Graph Mode                    | 🔴 NO plan     | 🔴 NO plan     | /                                                                      |
| Sleep Mode                    | 🟢 Functional  | 🟢 Functional  | [Usage Limits](https://github.com/vllm-project/vllm-ascend/issues/733) |
| MTP                           | 🟢 Functional  | 🟢 Functional  | [Usage Limits](https://github.com/vllm-project/vllm-ascend/issues/734) |
