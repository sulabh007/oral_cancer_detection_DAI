{"metadata":{"kernelspec":{"language":"python","display_name":"Python 3","name":"python3"},"language_info":{"name":"python","version":"3.10.13","mimetype":"text/x-python","codemirror_mode":{"name":"ipython","version":3},"pygments_lexer":"ipython3","nbconvert_exporter":"python","file_extension":".py"},"kaggle":{"accelerator":"none","dataSources":[],"dockerImageVersionId":30646,"isInternetEnabled":true,"language":"python","sourceType":"notebook","isGpuEnabled":false}},"nbformat_minor":4,"nbformat":4,"cells":[{"cell_type":"code","source":"import pandas as pd\nimport matplotlib.pyplot as plt\n\n\n\n###-----------------------------------\n### Function to plot Loss Curve\n###-----------------------------------\n\ndef plot_torch_hist(hist_df : pd.DataFrame):\n    '''\n    Args:\n      hist_df : pandas Dataframe with five columns\n                First column need to be epoch, 'x' values\n    '''\n    # instantiate figure\n    fig, axes = plt.subplots(1,2 , figsize = (15,6))\n\n    facecolor = 'cyan'\n    fontsize=12\n\n    # Get columns by index to eliminate any column naming error\n    x = \"epoch\"\n    y1 = \"train_loss\"\n    y2 = \"test_loss\"\n    y3 = \"train_acc\"\n    y4 = \"test_acc\"\n\n\n    # properties  matplotlib.patch.Patch\n    props = dict(boxstyle='round', facecolor=facecolor, alpha=0.5)\n\n    # Where was min loss\n    best = hist_df[hist_df[y2] == hist_df[y2].min()]\n\n    # pick first axis\n    ax = axes[0]\n\n    # Plot all losses\n    hist_df.plot(x = x, y = [y1,y2], ax = ax)\n\n    # little beautification\n    txtFmt = \"Loss: \\n  train: {:6.4f}\\n   test: {:6.4f}\"\n    txtstr = txtFmt.format(hist_df.iloc[-1][y1],\n                           hist_df.iloc[-1][y2]) #text to plot\n\n    # place a text box in upper middle in axes coords\n    ax.text(0.3, 0.95, txtstr,\n            transform=ax.transAxes,\n            fontsize=fontsize,\n            verticalalignment='top',\n            bbox=props)\n\n    # Mark arrow at lowest\n    offset = (best[y2].max() - best[y2].max())/10\n    ax.annotate(f'Min: {best[y2].to_numpy()[0]:6.4f}', # text to print\n                xy=(best[x].to_numpy(), best[y2].to_numpy()[0]), # Arrow start\n                xytext=(best[x].to_numpy()-2, best[y2].to_numpy()[0]+offset), # location of text\n                fontsize=fontsize, va='bottom', ha='right',bbox=props, # beautification of text\n                arrowprops=dict(facecolor=facecolor, shrink=0.05)) # arrow\n\n    # Draw vertical line at best value\n    ax.axvline(x = best[x].to_numpy(),\n               color = 'green',\n               linestyle='-.', lw = 3);\n\n    ax.set_xlabel(x.capitalize())\n    ax.set_ylabel(y1.capitalize())\n    ax.set_title('Errors')\n    ax.grid()\n    ax.legend(loc = 'upper left') # model legend to upper left\n\n    # pick second axis\n    ax = axes[1]\n\n    # Plot accuracy\n    hist_df.plot(x = x, y = [y3, y4], ax = ax)\n\n    # little beautification\n    txtFmt = \"Accuracy: \\n  train: {:6.4f}\\n  test:  {:6.4f}\"\n    txtstr = txtFmt.format(hist_df.iloc[-1][y3],\n                           hist_df.iloc[-1][y4]) #text to plot\n\n    # place a text box in lower middle in axes coords\n    ax.text(0.3, 0.2, txtstr,\n            transform=ax.transAxes, fontsize=fontsize,\n            verticalalignment='top', bbox=props)\n\n    # Mark arrow at lowest\n    offset = (best[y4].max() - best[y4].min())/10\n    ax.annotate(f'Best: {best[y4].to_numpy()[0]:6.4f}', # text to print\n                xy=(best[x].to_numpy(), best[y4].to_numpy()[0]), # Arrow start\n                xytext=(best[x].to_numpy()-2, best[y4].to_numpy()[0]-offset), # location of text\n                fontsize=fontsize, va='bottom', ha='right',bbox=props, # beautification of text\n                arrowprops=dict(facecolor=facecolor, shrink=0.05)) # arrow\n\n\n    # Draw a vertical line at best value\n    ax.axvline(x = best[x].to_numpy(),\n               color = 'green',\n               linestyle='-.', lw = 3)\n\n    # Labels\n    ax.set_xlabel(x.capitalize())\n    ax.set_ylabel(y3.capitalize())\n    ax.set_title('Accuracies')\n    ax.grid();\n    ax.legend(loc = 'lower left')\n\n    plt.tight_layout()\n\n\n\n\n    # pick first axis\n    ax = axes[0]\n\n    # Plot all losses\n    hist_df.plot(x = x, y = [y1,y2], ax = ax)\n\n    # little beautification\n    txtFmt = \"Loss: \\n  train: {:6.4f}\\n   test: {:6.4f}\"\n    txtstr = txtFmt.format(hist_df.iloc[-1][y1],\n                           hist_df.iloc[-1][y2]) #text to plot\n\n    # place a text box in upper middle in axes coords\n    ax.text(0.3, 0.95, txtstr,\n            transform=ax.transAxes,\n            fontsize=fontsize,\n            verticalalignment='top',\n            bbox=props)\n\n    # Mark arrow at lowest\n    offset = (best[y2].max() - best[y2].max())/10\n    ax.annotate(f'Min: {best[y2].to_numpy()[0]:6.4f}', # text to print\n                xy=(best[x].to_numpy(), best[y2].to_numpy()[0]), # Arrow start\n                xytext=(best[x].to_numpy()-2, best[y2].to_numpy()[0]+offset), # location of text\n                fontsize=fontsize, va='bottom', ha='right',bbox=props, # beautification of text\n                arrowprops=dict(facecolor=facecolor, shrink=0.05)) # arrow\n\n    # Draw vertical line at best value\n    ax.axvline(x = best[x].to_numpy(),\n               color = 'green',\n               linestyle='-.', lw = 3);\n\n    ax.set_xlabel(x.capitalize())\n    ax.set_ylabel(y1.capitalize())\n    ax.set_title('Errors')\n    ax.grid()\n    ax.legend(loc = 'upper left') # model legend to upper left\n\n    # pick second axis\n    ax = axes[1]\n\n    # Plot accuracy\n    hist_df.plot(x = x, y = [y3, y4], ax = ax)\n\n    # little beautification\n    txtFmt = \"Accuracy: \\n  train: {:6.4f}\\n  test:  {:6.4f}\"\n    txtstr = txtFmt.format(hist_df.iloc[-1][y3],\n                           hist_df.iloc[-1][y4]) #text to plot\n\n    # place a text box in lower middle in axes coords\n    ax.text(0.3, 0.2, txtstr,\n            transform=ax.transAxes, fontsize=fontsize,\n            verticalalignment='top', bbox=props)\n\n    # Mark arrow at lowest\n    offset = (best[y4].max() - best[y4].min())/10\n    ax.annotate(f'Best: {best[y4].to_numpy()[0]:6.4f}', # text to print\n                xy=(best[x].to_numpy(), best[y4].to_numpy()[0]), # Arrow start\n                xytext=(best[x].to_numpy()-2, best[y4].to_numpy()[0]-offset), # location of text\n                fontsize=fontsize, va='bottom', ha='right',bbox=props, # beautification of text\n                arrowprops=dict(facecolor=facecolor, shrink=0.05)) # arrow\n\n\n    # Draw a vertical line at best value\n    ax.axvline(x = best[x].to_numpy(),\n               color = 'green',\n               linestyle='-.', lw = 3)\n\n    # Labels\n    ax.set_xlabel(x.capitalize())\n    ax.set_ylabel(y3.capitalize())\n    ax.set_title('Accuracies')\n    ax.grid();\n    ax.legend(loc = 'lower left')\n    \n    plt.tight_layout()\n    \n    plt.savefig('/kaggle/working/plot.png')","metadata":{"_uuid":"8f2839f25d086af736a60e9eeb907d3b93b6e0e5","_cell_guid":"b1076dfc-b9ad-4769-8c92-a6c4dae69d19","execution":{"iopub.status.busy":"2024-02-13T11:24:07.742517Z","iopub.execute_input":"2024-02-13T11:24:07.743035Z","iopub.status.idle":"2024-02-13T11:24:07.771485Z","shell.execute_reply.started":"2024-02-13T11:24:07.743002Z","shell.execute_reply":"2024-02-13T11:24:07.770572Z"},"trusted":true},"execution_count":2,"outputs":[]}]}