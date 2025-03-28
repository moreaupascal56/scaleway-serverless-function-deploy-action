# Scaleway Serverless Function Deploy Github Action

This GitHub Action uses the Scaleway CLI to deploy your Functions in Scaleway Serverless.

## Usage
In your workflow use this Action like so, filling in the arguments with your own values.

```yml
      - name: Deploy function to Scaleway
        uses: moreaupascal56/scaleway-serverless-function-deploy-action@main
        with:
          function_dir: relative_path_to_the_dir_containing_your_function
          requirements_txt_path: relative_path_to_the_requirements.txt
          scw_function_name: your_function_name
          scw_namespace_id: your_scaleway_namespace_id
          scw_region: your_scaleway_region
          scw_runtime: your_scaleway_runtime
```

You will also need to add the Scaleway CLI Action: https://github.com/scaleway/action-scw
## Arguments

| Argument             | Description                                                                               | Required | Default |
|----------------------|-------------------------------------------------------------------------------------------|-----|---------|
| `function_dir`             | Relative path to the directory containing your function (ex. src)                         | ✔️     | N/A     |
| `requirements_txt_path`       | Relative path to the requirements.txt file (ex. requirements.txt if on your project root) | ✔️   | N/A     |
| `scw_function_name`         | The name (not ID) of your Serverless Function                                             | ✔️   | N/A     |
| `scw_namespace_id` | The ID of your Scaleway Function Namespace                                                | ✔️   | N/A     |
| `scw_region` | The Scaleway region                                                                       | ✔️     | fr-par  |
| `scw_runtime` | The runtime of your function                                                              | ✔️     | N/A     |

All the documentation for the `scw_` arguments can be find here: https://github.com/scaleway/scaleway-cli/blob/master/docs/commands/function.md#deploy-a-function

## Thanks

Inspired from https://github.com/yamatt/scaleway-serverless-container-deploy-action