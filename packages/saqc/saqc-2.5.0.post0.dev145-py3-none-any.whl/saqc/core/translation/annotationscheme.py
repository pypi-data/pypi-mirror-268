#! /usr/bin/env python

# SPDX-FileCopyrightText: 2021 Helmholtz-Zentrum für Umweltforschung GmbH - UFZ
#
# SPDX-License-Identifier: GPL-3.0-or-later

# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

from saqc.constants import UNFLAGGED
from saqc.core import DictOfSeries, Flags, History
from saqc.core.translation.basescheme import TranslationScheme


class Annotator(TranslationScheme):

    def __init__(self, scheme):
        self._scheme = scheme

    @property
    def DFILTER_DEFAULT(self):
        return self._scheme.DFILTER_DEFAULT

    def __call__(self, flag):
        return self._scheme.__call__(flag)

    def toExternal(self, flags: Flags, attrs: dict | None = None) -> DictOfSeries:
        tflags = self._scheme.toExternal(flags=flags, attrs=attrs)

        out = DictOfSeries()
        for field, df in tflags.items():
            if isinstance(df, pd.Series):
                df = df.to_frame(name="flag")

            history = flags.history[field]

            for col in history.columns:
                valid = (history.hist[col] != UNFLAGGED) & history.hist[col].notna()
                meta = history.meta[col]
                df.loc[valid, "func"] = meta["func"]
                df.loc[valid, "parameters"] = str(meta["kwargs"])
            df.loc[:, ("func", "parameters")] = df.loc[
                :, ("func", "parameters")
            ].fillna("")
            out[field] = df

        return out

    # def toInternal(self, flags: DictOfSeries) -> Flags:
    #     data = {}
    #     for key, frame in flags.items():
    #         tflags = self._scheme.toInternal(frame.drop(["func", "parameters"], axis=1))
    #         history = tflags.history[tflags.columns[0]]

    #         meta = [{}]*len(history.columns)
    #         # all func(parameters) groups represent one saqc function call
    #         # NOTE: func(parameters) that did not produce a final flag
    #         #       won't be present in the output History
    #         for (func, kwargs), values in frame.groupby(
    #             ["func", "parameters"]
    #         ):
    #             if not func and not kwargs:
    #                 continue

    #             # choose one of the rows where func(parameters) produced the final flag
    #             hist_row = history.hist.loc[values.index].iloc[0]
    #             print(hist_row)
    #             # find the history column that was produced by func(parameters)
    #             hist_col = _DEAGGREGATIONS[AGGREGATION](hist_row)
    #             meta[hist_col] = {"func": func, "args": (), "kwargs": kwargs}

    #         history.meta = meta
    #         data[key] = history
    #     return Flags(data)

    def toInternal(self, flags: DictOfSeries) -> Flags:

        tflags = self._scheme.toInternal(
            {k: v.drop(["func", "parameters"], axis=1) for k, v in flags.items()}
        )
        import ipdb

        ipdb.set_trace()
        data = {}
        for key, frame in flags.items():
            # tflags = self._scheme.toInternal(frame.drop(["func", "parameters"], axis=1))
            frame = pd.DataFrame(
                {
                    "flag": tflags.history[key].squeeze(raw=True),
                    "func": frame["func"],
                    "parameters": frame["parameters"],
                }
            )
            history = History(index=frame.index)
            for (flag, func, kwargs), values in frame.groupby(
                ["flag", "func", "parameters"]
            ):
                column = pd.Series(np.nan, index=frame.index)
                column.loc[values.index] = self(flag)
                history.append(column, meta={"func": func, "kwargs": kwargs})
            data[key] = history
        return Flags(data)
