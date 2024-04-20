# def fit(self,
#             func: Callable | str,
#             p0: npt.ArrayLike | None = None,
#             limits: tuple[float, ...] | None = None,
#             plot_result: bool = False,
#             params_names: List[str] | Tuple[str] | None = None):
#         """
#         Fit the bins content with the given function. The error is taken as the square root of the bin content.
#         Bins with 0 counts are ignored.
#
#         :param func: function to fit. If a string is given, the corresponding function if used
#         :param p0: initial values for the parameters
#         :param limits: (x_min, x_max)
#         :param plot_result: if True, the histogram with the fitted function, the covariance matrix and the normalised
#         residuals are plotted
#         :param params_names: if None, the parameters' names are inferred from the signature of the function
#         :return:
#         """
#
#         if limits is not None:
#             if len(limits) != 2:
#                 raise ValueError("Two expected")
#
#             bin_min = self.bins.find_bin_number(limits[0]) + 1
#             bin_max = self.bins.find_bin_number(limits[1]) + 1
#             x = self.X[bin_min: bin_max]
#             y = self.counts[bin_min: bin_max]
#             err_y = self.get_bins_errors()[bin_min: bin_max]
#         else:
#             x = self.X
#             y = self.counts
#             err_y = self.get_bins_errors()
#
#         idx_counts_non_zero = np.where(y > 0)[0]
#         x = x[idx_counts_non_zero]
#         y = y[idx_counts_non_zero]
#         err_y = err_y[idx_counts_non_zero]
#
#         if isinstance(func, str):
#             func_name = func
#             if func_name not in ff.mapping_names:
#                 raise KeyError(f"{func_name} not available. Function available are "
#                                f"{', '.join(list(ff.mapping_names.keys()))}")
#             func = ff.mapping_names[func_name]
#
#         param, cov, info_dict, msg, flag = curve_fit(func, xdata=x, ydata=y, p0=p0, sigma=err_y, full_output=True)
#
#         residuals = info_dict["fvec"]
#
#         chi_square = np.sum(np.power(residuals, 2))
#         nb_params = len(param)
#         nb_dof = x.size - nb_params
#
#         df_params = pd.DataFrame({
#             "params": params_names if params_names is not None else list(inspect.signature(func).parameters)[1:],
#             "value": param,
#             "error": np.sqrt(np.diag(cov)),
#         })
#         df_params["rel_error"] = df_params["error"] / df_params["value"] * 100
#
#         print(msg)
#         print(df_params)
#         print(f"chi square: {chi_square:.2f}")
#         print(f"ndof: {nb_dof:>12}")
#
#         if plot_result:
#             plt.figure()
#             plt.errorbar(x=x, y=y,
#                          xerr=self.bins.bins_widths[idx_counts_non_zero] / 2,
#                          yerr=err_y, capsize=2, fmt='none', label='counts')
#             t = np.linspace(x[0], x[-1], 100)
#             y_func = [func(a, *param) for a in t]
#             plt.plot(t, y_func, c='r', linewidth=2, label='fit')
#             plt.grid(alpha=0.5)
#             # plt.text(0.7*t.max(), 0.7*y.max(), fr"$\chi^2$: {chi_square:.2f}",
#             #          bbox={"boxstyle": "round", "ec": [0.4, 0.4, 0.4], "fc": "#f6ede4"})
#             plt.legend()
#
#             # covariance matrix
#             plt.figure()
#             im = plt.imshow(cov, origin="lower", extent=[0, nb_params, 0, nb_params])
#             ticks_loc = [0.5 + i for i in range(nb_params)]
#             ticks_labels = params_names if params_names is not None else list(inspect.signature(func).parameters)[1:]
#             plt.xticks(ticks_loc, labels=ticks_labels)
#             plt.yticks(ticks_loc, labels=ticks_labels)
#             plt.colorbar(im)
#
#             plt.title("Covariance matrix", fontsize=12, fontweight="bold", pad=15)
#
#             # histogram of the residuals
#             plt.figure()
#             bin_width = 0.5
#             x_min, x_max = round(residuals.min() - 1), round(residuals.max() + 1)
#             max_x = max(abs(x_min), abs(x_max))
#             if max_x > 5:
#                 plt.xlim(-max_x, max_x)
#             else:
#                 plt.xlim(-5, 5)  # +/- 5 sigma
#
#             plt.hist(residuals, bins=np.arange(x_min, x_max + bin_width, bin_width), density=True, alpha=0.7)
#             plt.plot(u := np.linspace(-5, 5, 101), norm.pdf(u), linewidth=2,
#                      label="Expected distribution")
#             plt.legend()
#             plt.grid(alpha=0.5)
#             plt.title("Distribution of the normalised residuals", fontsize=12, fontweight="bold",
#                       pad=15)
#
#         return param, cov, info_dict