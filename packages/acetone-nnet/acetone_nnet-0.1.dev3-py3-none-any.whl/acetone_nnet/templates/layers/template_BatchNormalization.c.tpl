    //{{name}}_{{idx}}{{comment}}
    for(f = 0; f < {{input_channels}}; ++f)
    {
        for(k = 0; k < {{channel_size}}; ++k)
        {
            output_{{path}}[k + {{input_channels}}*f] = scale_{{name}}_{{idx}}*({{output_str}}[k + {{input_channels}}*f] - mean_{{name}}_{{idx}}[f])/sqrt(var_{{name}}_{{idx}}[f] + {{epsilon}}) + biases_{{name}}_{{idx}}[f];
            {{#activation_function}}
            output_{{path}}[k + {{input_channels}}*f] = {{{activation_function}}};
            {{/activation_function}}
        }
    }