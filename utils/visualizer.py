import matplotlib.pyplot as plt

def visualize_query_result(df):
    if df.empty or df.shape[1] < 2:
        print("[Visualization] DataFrame is empty or has fewer than 2 columns.")
        return None

    try:
        x_col = df.columns[0]
        y_cols = df.select_dtypes(include=['number']).columns.tolist()

        print(f"[Visualization] x_col: {x_col}")
        print(f"[Visualization] y_cols: {y_cols}")

        if not y_cols:
            print("[Visualization] No numeric columns found.")
            return None

        y_col = y_cols[0]

        fig, ax = plt.subplots(figsize=(10, 5))
        df.plot(x=x_col, y=y_col, kind='bar', ax=ax)

        ax.set_title(f"{y_col} by {x_col}")
        plt.xticks(rotation=45)
        plt.tight_layout()
        return fig

    except Exception as e:
        print(f"[Visualization Error] {e}")
        return None
