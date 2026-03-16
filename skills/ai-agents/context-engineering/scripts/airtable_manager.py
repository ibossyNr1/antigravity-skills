import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv
from pyairtable import Api

# Load environment variables
load_dotenv()

class AirtableManager:
    def __init__(self):
        self.api_key = os.getenv("AIRTABLE_API_KEY")
        self.base_id = os.getenv("AIRTABLE_BASE_ID")
        
        if not self.api_key or not self.base_id:
            print("❌ Error: AIRTABLE_API_KEY or AIRTABLE_BASE_ID not found in .env")
            sys.exit(1)
            
        self.api = Api(self.api_key)
        self.base = self.api.base(self.base_id)

    def sync_record(self, table_name, fields):
        """Sync a single record to a specific table."""
        try:
            table = self.base.table(table_name)
            record = table.create(fields)
            print(f"✅ Success: Record synced to {table_name} (ID: {record['id']})")
            return record
        except Exception as e:
            print(f"❌ Error syncing to Airtable: {str(e)}")
            return None

    def log_event(self, event_type, description, metadata=None):
        """Specifically log an agentic event/decision."""
        fields = {
            "Timestamp": datetime.utcnow().isoformat(),
            "Event Type": event_type,
            "Description": description,
            "Metadata": json.dumps(metadata) if metadata else "{}"
        }
        return self.sync_record("Agent Logs", fields)

    def sync_research(self, topic, summary, sources=None):
        """Sync research findings."""
        fields = {
            "Date": datetime.utcnow().strftime("%Y-%m-%d"),
            "Topic": topic,
            "Summary": summary,
            "Sources": ", ".join(sources) if sources else ""
        }
        return self.sync_record("Research", fields)

def main():
    parser = argparse.ArgumentParser(description="Airtable Manager for Context Engineering")
    subparsers = parser.add_subparsers(dest="command", help="Sub-commands")

    # Log command
    log_parser = subparsers.add_parser("log", help="Log an event")
    log_parser.add_argument("--type", required=True, help="Type of event")
    log_parser.add_argument("--desc", required=True, help="Description of the event")
    log_parser.add_argument("--meta", help="JSON metadata")

    # Research command
    res_parser = subparsers.add_parser("research", help="Sync research")
    res_parser.add_argument("--topic", required=True, help="Research topic")
    res_parser.add_argument("--summary", required=True, help="Research summary")
    res_parser.add_argument("--sources", help="Comma-separated sources")

    args = parser.parse_args()
    manager = AirtableManager()

    if args.command == "log":
        meta = json.loads(args.meta) if args.meta else None
        manager.log_event(args.type, args.desc, meta)
    elif args.command == "research":
        sources = args.sources.split(",") if args.sources else None
        manager.sync_research(args.topic, args.summary, sources)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
