import pandas as pd

class QueryHandler:
    def __init__(self, data=None):
        self.data = data

    def handle_summarize_data(self, query=None):
        if self.data is not None:
            summary_lines = []
            summary_lines.append("### 📊 Data Summary Report\n")

            for column in self.data.columns:
                dtype = self.data[column].dtype

                if pd.api.types.is_numeric_dtype(dtype):
                    # Check if values look like years
                    if self.data[column].between(1900, 2100, inclusive="both").all():
                        top_values = self.data[column].value_counts().nlargest(3).index.tolist()
                        summary_lines.append(
                            f"**Column: {column}** (Numeric - Year)\n"
                            + "\n".join([f"- {i+1}. {v}" for i, v in enumerate(top_values)]) + "\n"
                        )
                    else:
                        top_values = self.data[column].nlargest(3).tolist()
                        bottom_values = self.data[column].nsmallest(3).tolist()
                        summary_lines.append(
                            f"**Column: {column}** (Numeric)\n"
                            f"Top 3 Values:\n" + "\n".join([f"- {i+1}. {v}" for i, v in enumerate(top_values)]) + "\n"
                            f"Bottom 3 Values:\n" + "\n".join([f"- {i+1}. {v}" for i, v in enumerate(bottom_values)]) + "\n"
                        )

                elif pd.api.types.is_string_dtype(dtype):
                    top_values = self.data[column].value_counts().nlargest(3).index.tolist()
                    summary_lines.append(
                        f"**Column: {column}** (Text)\n"
                        f"Top 3 Most Frequent:\n" + "\n".join([f"- {i+1}. {v}" for i, v in enumerate(top_values)]) + "\n"
                    )

                elif pd.api.types.is_datetime64_any_dtype(dtype):
                    top_values = self.data[column].value_counts().nlargest(3).index.tolist()
                    summary_lines.append(
                        f"**Column: {column}** (DateTime)\n"
                        f"Top 3 Most Frequent Dates:\n" + "\n".join([f"- {i+1}. {v}" for i, v in enumerate(top_values)]) + "\n"
                    )

                else:
                    summary_lines.append(
                        f"**Column: {column}** ({dtype})\n"
                        f"- Unique Values: {self.data[column].nunique()}\n"
                    )

            return "\n".join(summary_lines)

        return "⚠️ No data available to summarize. Please upload a file first."