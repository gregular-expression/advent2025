FROM python:3.12-slim

WORKDIR /app

# Install dependencies for puzzle_day_1
COPY puzzle_day_1/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project so puzzle_day_1 and shared resources (like input.txt) are available
COPY . .

CMD ["python", "-m", "puzzle_day_1.main"]


