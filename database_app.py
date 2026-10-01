import time

class DynamicSchemaIntegrityEngine:
    """
    Enterprise-grade Data Schema Validation Matrix.
    Engineered with strict key-type constraints to enforce
    data layer integrity and prevent runtime crashes cleanly.
    """
    def __init__(self, expected_schema: dict):
        self.expected_schema = expected_schema
        print("⚙️ [Initialization] Dynamic Schema Integrity Engine locked safely in memory.")

    def validate_data_payload(self, raw_payload: dict) -> bool:
        """
        Validates incoming data dictionary structures against the expected schema definitions.
        Executes with strict O(K) lookup efficiency to guarantee high throughput.
        """
        for field_name, expected_type in self.expected_schema.items():
            # Rule 1: Check for missing critical field keys safely
            if field_name not in raw_payload:
                print(f"❌ [Schema Failure] Missing required transaction key field: '{field_name}'")
                return False
                
            actual_value = raw_payload[field_name]
            
            # Rule 2: Enforce strict type validation limits to prevent system pollution
            if not isinstance(actual_value, expected_type):
                print(f"❌ [Type Mismatch] Field '{field_name}' expects {expected_type.__name__}, got {type(actual_value).__name__} instead.")
                return False
                
        return True

if __name__ == "__main__":
    print("🚀 Starting Sudhir's Dynamic Schema Integrity Validation Matrix [Day 28]...\n")
    
    # Define an ironclad target blueprint structure for a doctor registration form
    target_medical_blueprint = {
        "doctor_id": int,
        "name": str,
        "specialty": str,
        "is_active": bool
    }
    
    validator = DynamicSchemaIntegrityEngine(target_medical_blueprint)
    
    # Testing an incoming malformed user payload structure containing bad types
    corrupted_incoming_packet = {
        "doctor_id": 105,
        "name": "DR. ANAND MISHRA",
        "specialty": "NEUROLOGIST",
        "is_active": "True" # Intentionally injected as a String instead of a proper Boolean flag
    }
    
    start_benchmark = time.perf_counter()
    
    # Fire the live validation test routine execution sweep
    is_schema_valid = validator.validate_data_payload(corrupted_incoming_packet)
    
    end_benchmark = time.perf_counter()
    duration_ms = (end_benchmark - start_benchmark) * 1000
    
    print("-" * 85)
    print(f"🛡️ Core Data Payload Integrity Matrix Status : {'🟢 PASS - 100% SECURE' if is_schema_valid else '🚨 CRITICAL MATCH REJECTED'}")
    print(f"⚡ Structural Schema Verification Latency  : {duration_ms:.4f} ms")
    print("-" * 85)
    print("\n🎉 Dynamic validator engine execution cycle completed with absolute layout safety!")